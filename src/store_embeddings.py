import chromadb
from create_embeddings import create_embeddings
from config import CHROMA_PATH, COLLECTION_NAME

def store_embeddings():
    chunks = create_embeddings()

    client = chromadb.PersistentClient(path=CHROMA_PATH)
    collection = client.get_or_create_collection(name=COLLECTION_NAME)

    for chunk in chunks:
        collection.add(
            ids=[chunk["chunk_id"]],
            embeddings=[chunk["embedding"].tolist()],
            documents=[chunk["text"]],
            metadatas=[{"source": chunk["source"]}]
        )

    print(f"Stored {len(chunks)} chunks in ChromaDB.")
    return collection


if __name__ == "__main__":
    store_embeddings()