import os
from dotenv import load_dotenv

load_dotenv()

# Google Gemini API key
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")

# Gemini model
GEMINI_MODEL = "gemini-3.8-flash"

# Local embedding model
EMBEDDING_MODEL = "BAAI/bge-small-en-v1.5"

# RAG settings
CHUNK_SIZE = 800
CHUNK_OVERLAP = 150
TOP_K = 4

# ChromaDB settings
VECTOR_DB_PATH = "./vectorstore"
COLLECTION_NAME = "knowledge_base"