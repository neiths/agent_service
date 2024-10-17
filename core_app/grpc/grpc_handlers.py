import time
import grpc
import traceback
import face_recognition
from faster_whisper import WhisperModel
import pyaudio 
import numpy as np
import io
import os
from io import BytesIO
import torch  # Add this import
# grpc handlers
from concurrent import futures
from core_app.grpc.pb import ocr_service_pb2, ocr_service_pb2_grpc, stt_service_pb2, stt_service_pb2_grpc, face_recognition_pb2, face_recognition_pb2_grpc
from pdfminer.high_level import extract_text
from core_app.pdf_classify.pdf_classify import is_scanned_pdf, process_scanned_pdf_with_llm, get_image_informations
from PIL import Image
import logging
from core_app.models import FaceData

logging.basicConfig(filename='document_processing.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
logger = logging.getLogger(__name__)

def get_file_extension(file_path):
    _, file_extension = os.path.splitext(file_path)
    return file_extension

def whisper_model(model_size, device=None):
    if device is None:
        if torch.cuda.is_available():
            device = 'cuda'
            compute_type = 'float16'
        else:
            device = 'cpu'
            compute_type = 'int8' 

    model = WhisperModel(model_size_or_path=model_size, device=device, compute_type=compute_type)
    return model

def transcribe_audio(audio_stream, init_prompt=None):
    model = whisper_model(model_size='base')
    try:
        segments, info = model.transcribe(audio=audio_stream, initial_prompt=init_prompt, beam_size=3, word_timestamps=True, condition_on_previous_text=True)
        transcription = " ".join([segment.text for segment in segments])
        return transcription.strip()
    except Exception as e:
        return "Error during transcription"

class OCRServiceServicer(ocr_service_pb2_grpc.OCRServiceServicer):

    def CreateTextFromFile(self, request, context):
        try:
            file_name = request.file_name
            pdf = request.file
            text = None

            logger.info(f"Processing file: {file_name}")

            if is_scanned_pdf(pdf):
                # if scanned PDF => vision LLM model
                file_name = file_name.lower()
                if file_name.endswith('.pdf'):
                    logger.info("The file is a scanned PDF.")
                    text = process_scanned_pdf_with_llm(pdf)
                elif file_name.endswith(('.png', '.jpg', '.jpeg')):
                    logger.info("The file is an image.")
                    image = Image.open(BytesIO(pdf))
                    text = get_image_informations(image)
                else:
                    logger.warning("Unsupported file format.")
                    return ocr_service_pb2.FileResponse(
                        message = "Unsupported file format",
                        text = ""
                        )
            else:
                logger.info("The file is a regular PDF with extractable text.")
                file_like_object = BytesIO(pdf)
                text = extract_text(file_like_object)

            if text.startswith("ERROR:"):
                if "too small" in text.lower() or "unclear" in text.lower():
                    logger.warning(f"Problem: {text}")
                    return ocr_service_pb2.FileResponse(
                        message = "error.image-too-small-or-unclear",
                        text = ""
                        )
                else:
                    logger.warning(f"Error during OCR processing: {text}")
                    return ocr_service_pb2.FileResponse(
                        message = "error.can-not-read-file",
                        text = text
                        )
                    
            logger.info(f"Successfully processed file: {file_name}")
            return ocr_service_pb2.FileResponse(
                message = "", 
                text = text
                )
        
        except Exception as e:
            logger.error(f"Error during OCR processing for file {file_name}: {e}")
            return ocr_service_pb2.FileResponse(
                message = "error.unknown-error",
                text = "noooo"
                )

class STTServiceServicer(stt_service_pb2_grpc.STTServiceServicer):

    def UploadAudio(self, request, context):
        start_time = time.time()

        audio_data = io.BytesIO(request.file_data)

        logger.info("Starting audio transcription for uploaded file.")
        
        try:
            transcription = transcribe_audio(audio_data)
            logger.info("Successfully transcribed uploaded audio file.")
        except Exception as e:
            logger.error(f"Error during audio transcription: {e}")
            return stt_service_pb2.TranscriptionResponse(transcription="Error during transcription")
        
        end_time = time.time()
        total_time = end_time - start_time
        
        logger.info(f"Total processing time for uploaded audio: {total_time:.2f} seconds")


        return stt_service_pb2.TranscriptionResponse(transcription=transcription)

    def StreamAudio(self, request_iterator, context):
        audio_stream = io.BytesIO()
        buffer_size = 1024  * 32# Example buffer size (10KB)
        buffer = bytearray()
        init_prompt = ""
        
        start_time = time.time()

        logger.info("Starting streaming audio transcription.")

        try:
            for chunk in request_iterator:
                if not chunk.chunk_data:
                    continue
                
                buffer.extend(chunk.chunk_data)
                
                # If the buffer reaches the defined size, process it
                if len(buffer) >= buffer_size:
                    audio_stream.write(buffer)
                    audio_stream.seek(0)

                    try:
                        transcription = transcribe_audio(audio_stream, init_prompt)
                        init_prompt += transcription
                        init_prompt = init_prompt[-100:]
                        
                        logger.info(f"Transcribed chunk: {transcription}")

                        yield stt_service_pb2.TranscriptionStreamingResponse(transcription=transcription)
                    except Exception as e:
                        logger.error(f"Error during chunk transcription: {e}")
                        yield stt_service_pb2.TranscriptionStreamingResponse(transcription="Error during transcription")

                    # Clear the buffer for the next set of chunks
                    buffer.clear()

                    # Move the stream cursor to the end to prepare for more data
                    audio_stream.seek(0, io.SEEK_END)

            # Process any remaining data in the buffer after the stream ends
            if buffer:
                audio_stream.write(buffer)
                audio_stream.seek(0)
                try:
                    transcription = transcribe_audio(audio_stream, init_prompt)
                    logger.info(f"Final chunk transcription: {transcription}")
                    yield stt_service_pb2.TranscriptionStreamingResponse(transcription=transcription)
                except Exception as e:
                    logger.error(f"Error during final transcription: {e}")
                    yield stt_service_pb2.TranscriptionStreamingResponse(transcription="Error during transcription")

        except Exception as e:
            logger.error(f"Error during audio streaming: {e}")
            return "Error: during the streaming"
        finally:
            audio_stream.close()

        end_time = time.time()
        total_time = end_time - start_time
        logger.info(f"Total processing time for audio streaming: {total_time:.2f} seconds")

class FaceRecognitionService(face_recognition_pb2_grpc.FaceRecognitionService):
    def UploadImage(self, request, context):
        """Nhận ảnh từ người dùng, mã hóa và lưu nếu chưa có."""
        try:
            # Lấy dữ liệu từ request
            file_data = request.file_data
            country = request.Country
            full_name = request.FullName
            birthday = request.Birthday
            gender = request.Gender
            age = request.Age
            email = request.Email
            phone_number = request.Phone_number
            
            if FaceData.objects.filter(full_name=full_name).exists():
                logger.info(f"Face already exists: {full_name}.")
                return face_recognition_pb2.UploadImageResponse(message= f"Full name: {full_name} already exists in the database.")

            logger.info(f"Received image from {full_name} in {country}.")

            # Đọc và mã hóa ảnh
            image_np = face_recognition.load_image_file(BytesIO(file_data))
            face_encodings = face_recognition.face_encodings(image_np)

            if not face_encodings:
                logger.info("No face detected in the image.")
                return face_recognition_pb2.UploadImageResponse(message="No face detected in the image.")

            face_encoding = face_encodings[0]

            # Lấy tất cả các mã hóa khuôn mặt đã biết từ database và tên tương ứng    
            existing_faces = FaceData.objects.all()
            known_face_encodings = [np.frombuffer(face.encoding) for face in existing_faces]
            known_face_names = [face.full_name for face in existing_faces]
            
            # So sánh với danh sách khuôn mặt đã biết
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)

            if matches:
                best_match_index = np.argmin(face_distances)
                if matches[best_match_index]:
                    name = known_face_names[best_match_index]
                    logger.info(f"Face recognized: {name}")
                    return face_recognition_pb2.UploadImageResponse(message=f"Face already exists: {name} in {country}.")

            face_record = FaceData(
                full_name=full_name,
                country=country,
                birthday=birthday,
                gender = gender,
                age = age,
                email = email,
                phone_number = phone_number,
                encoding=face_encoding.tobytes(),
            )
            face_record.image.save(f"{full_name}.png", BytesIO(file_data))
            face_record.save()
                
            logger.info(f"New face added: {full_name}")

            return face_recognition_pb2.UploadImageResponse(message=f"Image received from {full_name} in {country}.")

        except Exception as e:
            logger.error(f"Error processing image from {full_name}: {e}")
            return face_recognition_pb2.UploadImageResponse(message="Error occurred during image processing.")
    
    def UploadImageRecognition(self, request, context):
        """Nhận ảnh và trả về danh sách khuôn mặt đã nhận dạng được cùng thông tin chi tiết."""
        try:
            # Lấy dữ liệu từ request
            file_data = request.file_data
            logger.info("Received image for recognition.")

            # Đọc và mã hóa ảnh
            logger.info("Loading image from request data.")
            image_np = face_recognition.load_image_file(BytesIO(file_data))
            face_locations = face_recognition.face_locations(image_np)
            face_encodings = face_recognition.face_encodings(image_np, face_locations)
            logger.info(f"Detected {len(face_locations)} face(s) in the image.")
            
            # Kiểm tra nếu không phát hiện được khuôn mặt nào
            if not face_encodings:
                logger.warning("No face encodings found for the detected faces.")
                return face_recognition_pb2.DetailResponse(
                    message="No face detected in the image.",
                    status_code=400
                )

            # Lấy danh sách khuôn mặt đã lưu trong cơ sở dữ liệu
            existing_faces = FaceData.objects.all()
            if not existing_faces.exists():
                logger.warning("No faces found in the database.")
                return face_recognition_pb2.DetailResponse(
                    message="No faces available in the database for comparison.",
                    status_code=404
                )

            # Chuyển các khuôn mặt từ database thành danh sách và mã hóa
            existing_faces_list = list(existing_faces)
            known_face_encodings = [np.frombuffer(face.encoding) for face in existing_faces]
            logger.info(f"Loaded {len(existing_faces)} existing faces from the database.")

            matched_faces = []
            for face_encoding in face_encodings:
                logger.info("Comparing detected face with known faces.")
                matches = face_recognition.compare_faces(known_face_encodings, face_encoding)
                face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
                
                if True in matches:
                    best_match_index = np.argmin(face_distances)
                    logger.info(f"Best match index: {best_match_index}, Distance: {face_distances[best_match_index]}")

                    if matches[best_match_index]:
                        matched_face = existing_faces_list[best_match_index]
                        logger.info(f"Face recognized: {matched_face.full_name}")

                        matched_face_instance = FaceData.objects.filter(full_name=matched_face.full_name).first()
                        
                        if matched_face_instance:
                            person_details = face_recognition_pb2.PersonDetails(
                                Country=matched_face_instance.country,
                                FullName=matched_face_instance.full_name,
                                Birthday=matched_face_instance.birthday.isoformat(),
                                Gender=matched_face_instance.gender,
                                Age=matched_face_instance.age,
                                Email=matched_face_instance.email,
                                Phone_number=matched_face_instance.phone_number
                            )
                            logger.info(f"Face recognized details: {person_details}")
                            matched_faces.append(person_details)

            if matched_faces:
                logger.info(f"Total recognized faces: {len(matched_faces)}")
                return face_recognition_pb2.DetailResponse(
                    message=f"Faces recognized: {matched_face.full_name}",
                    status_code=200,
                    persons=matched_faces
                )
            else:
                # Nếu không có khuôn mặt nào khớp
                logger.warning("No matching faces found in the database.")
                return face_recognition_pb2.DetailResponse(
                    message="No matching faces found.",
                    status_code=404
                )

        except Exception as e:
            logger.error(f"Error during face recognition: {e}")
            logger.error(traceback.format_exc())
            return face_recognition_pb2.DetailResponse(
                message="Error occurred during face recognition.",
                status_code=500
            )