import base64
from pydantic import BaseModel, Field
from langchain.chains import TransformChain
from langchain_core.messages import HumanMessage
from langchain_openai import ChatOpenAI
from langchain import globals
from langchain_core.runnables import chain
from langchain_core.output_parsers import JsonOutputParser
from io import BytesIO
from PIL import Image
import logging
logger = logging.getLogger(__name__)

# globals.set_debug(True)

def encode_image(image: Image.Image) -> dict:
    """Encode a PIL image as base64 and return in a dict with a proper format."""
    if image.mode in ['RGBA', 'P']:
        image = image.convert('RGB')
    
    buffered = BytesIO()
    image.save(buffered, format="JPEG")
    image_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    
    return {
        "url": f"data:image/jpeg;base64,{image_base64}"
    }

@chain
def image_model(inputs: dict) -> str | list[str] | dict:
    """Invoke model with image and prompt."""
    model = ChatOpenAI(temperature=0, model="gpt-4-turbo", max_tokens=1024)
    
    # Create a HumanMessage with both text and image content
    msg = model.invoke(
        [HumanMessage(
            content=[
                {"type": "text", "text": inputs["prompt"]},
                {"type": "image_url", "image_url": {"url": inputs['image']['url']}}
            ]
        )]
    )
    return msg.content

# parser = JsonOutputParser(pydantic_object=ImageInformation)

def get_image_informations(image: Image.Image, lang_key:str) -> dict:
    logger.info("Starting text extraction from image.")

    vision_prompt = f"""Given the image, extract all visible text, including any text present in the image.
         Make sure to include every piece of text visible in the image, regardless of its position or context.
        - Provide the text exactly as it appears, without any modifications or translations.
        - If handwriting is present, extract handwriting as accurately as possible.

        However, if the text is unclear, unreadable, or if the image lacks clarity, you must respond with "ERROR: " followed by an appropriate message, for example:
        "ERROR: The image is too small or blurry to extract readable text."
        "ERROR: The image does not contain visible text to extract."

        Rules:
        1. Only extract text if it is visible and readable.
        2. If the image or file is unclear, use the "ERROR: " prefix in your response and translate the error message according language key: {lang_key}
        3. Do not invent or add text that isn't present.
        """
    
    logger.info("Encoding image for Vision LLM processing.")
    # Encode the image
    image_data = encode_image(image)
    
    # Combine encoding, processing, and parsing into a single chain
    vision_chain = image_model
    
    logger.info("Invoking Vision LLM model with prompt.")
    # Execute the chain with the encoded image and prompt
    return vision_chain.invoke({
        'image': image_data,
        'prompt': vision_prompt
    })
    
def support_informations_LLM(text:str, image: Image.Image) -> dict:
    logger.info("Starting text extraction from image.")

    vision_prompt = f"""Given the extracted text from the image below, please review the image and improve it by correcting any spelling, grammar, or formatting issues without adding any new information.
            - Correct any spelling, grammar, or formatting errors and structure the text properly.
            Do not add or infer anything that is not already present in the extracted text. 
            Here is the text extracted from the image:
            {text}
            IMPORTANT: output only the corrected text, do not include the original text in your response.
        """
    
    logger.info("Encoding image for Vision LLM processing.")
    # Encode the image
    image_data = encode_image(image)
    
    # Combine encoding, processing, and parsing into a single chain
    vision_chain = image_model
    
    logger.info("Invoking Vision LLM model with prompt.")
    # Execute the chain with the encoded image and prompt
    return vision_chain.invoke({
        'image': image_data,
        'prompt': vision_prompt
    })