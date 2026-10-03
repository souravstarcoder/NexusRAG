from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma

from config import EMBEDDING_MODEL, VECTOR_DB_PATH, COLLECTION_NAME, TOP_K


def get_vector_db():
    embeddings = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
    )

    vector_db = Chroma(
        collection_name=COLLECTION_NAME,
        embedding_function=embeddings,
        persist_directory=VECTOR_DB_PATH
    )

    return vector_db


def search_knowledge_base(query):
    vector_db = get_vector_db()

    results = vector_db.similarity_search(
        query,
        k=TOP_K
    )

    return results


if __name__ == "__main__":

    query = input("Ask a question: ")

    results = search_knowledge_base(query)

    print("\n--- Retrieved Knowledge ---\n")

    if not results:
        print("No relevant information found.")
    else:
        for i, doc in enumerate(results, 1):
            print(f"\nResult {i}:")
            print(doc.page_content)