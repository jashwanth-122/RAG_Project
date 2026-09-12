from chunk_documents import chunk_documents
from embedding_model import get_embedding_model

def create_embeddings():
    chunks = chunk_documents()
    model = get_embedding_model()

    texts = [chunk["text"] for chunk in chunks]
    embeddings = model.encode(texts, show_progress_bar=True)

    for chunk, embedding in zip(chunks, embeddings):
        chunk["embedding"] = embedding

    return chunks


if __name__ == "__main__":
    chunks_with_embeddings = create_embeddings()
    print(f"\nCreated embeddings for {len(chunks_with_embeddings)} chunks.")
    first = chunks_with_embeddings[0]
    print(f"Example: {first['chunk_id']}")
    print(f"Embedding length: {len(first['embedding'])} numbers")