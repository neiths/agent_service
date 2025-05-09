from langchain_openai import OpenAIEmbeddings
from core_app.models import ExternalKnowledge
from langchain_core.retrievers import BaseRetriever
from core_app.models import ExternalKnowledge, InternalKnowledge
import os

embeddings_model = OpenAIEmbeddings(api_key=os.getenv("OPENAI_API_KEY"))

def get_vector_from_embedding(text):
    return embeddings_model.embed_query(text)
