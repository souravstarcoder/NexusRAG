from pathlib import Path

from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config import EMBEDDING_MODEL, CHUNK_SIZE, CHUNK_OVERLAP, VECTOR_DB_PATH


# -----------------------------
# 1. Load documents
# -----------------------------
def load_documents():
    documents = []
    data_folder = Path("data")

    for file_path in data_folder.iterdir():

        if file_path.suffix.lower() == ".txt":
            loader = TextLoader(
                str(file_path),
                encoding="utf-8"
            )
            documents.extend(loader.load())

        elif file_path.suffix.lower() == ".pdf":
            loader = PyPDFLoader(str(file_path))
            documents.extend(loader.load())

    return documents


# -----------------------------
# 2. Split documents into chunks
# -----------------------------
def split_documents(documents):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=CHUNK_SIZE,
        chunk_overlap=CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)


# -----------------------------
# 3. Create embeddings
# -----------------------------
def create_vector_database(chunks):

    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vector_db = Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=VECTOR_DB_PATH,
        collection_name="knowledge_base"
    )

    return vector_db


# -----------------------------
# Main pipeline
# -----------------------------
if __name__ == "__main__":

    print("Loading documents...")
    documents = load_documents()

    if not documents:
        print("No documents found inside the data folder.")
        exit()

    print(f"Loaded {len(documents)} document pages/files.")

    print("Splitting documents into chunks...")
    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks.")

    print("Creating embeddings and storing in ChromaDB...")
    create_vector_database(chunks)

    print("✅ Knowledge base created successfully!")
    print(f"Vector database location: {VECTOR_DB_PATH}")