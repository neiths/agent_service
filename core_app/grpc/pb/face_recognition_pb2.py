# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: face_recognition.proto
# Protobuf Python Version: 4.25.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x16\x66\x61\x63\x65_recognition.proto\x12\x02pb\"\\\n\x12UploadImageRequest\x12\x11\n\tfile_data\x18\x01 \x01(\x0c\x12\x10\n\x08\x46ullName\x18\x02 \x01(\t\x12\x0e\n\x06Gender\x18\x03 \x01(\t\x12\x11\n\tsubsystem\x18\x04 \x01(\t\"O\n\x13UploadImageResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\x12\n\nerror_code\x18\x03 \x01(\t\"%\n\x10ImageRecognition\x12\x11\n\tfile_data\x18\x01 \x01(\x0c\"1\n\rPersonDetails\x12\x10\n\x08\x46ullName\x18\x01 \x01(\t\x12\x0e\n\x06Gender\x18\x02 \x01(\t\"n\n\x0e\x44\x65tailResponse\x12\x0f\n\x07message\x18\x01 \x01(\t\x12\x13\n\x0bstatus_code\x18\x02 \x01(\x05\x12\"\n\x07persons\x18\x03 \x03(\x0b\x32\x11.pb.PersonDetails\x12\x12\n\nerror_code\x18\x04 \x01(\t2\x9c\x01\n\x16\x46\x61\x63\x65RecognitionService\x12>\n\x0bUploadImage\x12\x16.pb.UploadImageRequest\x1a\x17.pb.UploadImageResponse\x12\x42\n\x16UploadImageRecognition\x12\x14.pb.ImageRecognition\x1a\x12.pb.DetailResponseb\x06proto3')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'face_recognition_pb2', _globals)
if _descriptor._USE_C_DESCRIPTORS == False:
  DESCRIPTOR._options = None
  _globals['_UPLOADIMAGEREQUEST']._serialized_start=30
  _globals['_UPLOADIMAGEREQUEST']._serialized_end=122
  _globals['_UPLOADIMAGERESPONSE']._serialized_start=124
  _globals['_UPLOADIMAGERESPONSE']._serialized_end=203
  _globals['_IMAGERECOGNITION']._serialized_start=205
  _globals['_IMAGERECOGNITION']._serialized_end=242
  _globals['_PERSONDETAILS']._serialized_start=244
  _globals['_PERSONDETAILS']._serialized_end=293
  _globals['_DETAILRESPONSE']._serialized_start=295
  _globals['_DETAILRESPONSE']._serialized_end=405
  _globals['_FACERECOGNITIONSERVICE']._serialized_start=408
  _globals['_FACERECOGNITIONSERVICE']._serialized_end=564
# @@protoc_insertion_point(module_scope)
