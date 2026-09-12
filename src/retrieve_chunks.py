import chromadb
from embedding_model import get_embedding_model
from config import CHROMA_PATH, COLLECTION_NAME, TOP_K

def retrieve_chunks(question, top_k=TOP_K):
    model = get_embedding_model()
    question_embedding = model.encode([question])[0].tolist()

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    results = collection.query(
        query_embeddings=[question_embedding],
        n_results=top_k
    )

    return results


if __name__ == "__main__":
    question = "What model did I use for the churn prediction project?"
    results = retrieve_chunks(question)

    print(f"Question: {question}\n")
    print("Top matching chunks:")
    for doc, metadata in zip(results["documents"][0], results["metadatas"][0]):
        print(f"\nFrom: {metadata['source']}")
        print(doc[:200] + "...")