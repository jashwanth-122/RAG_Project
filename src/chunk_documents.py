from load_documents import load_documents
from config import CHUNK_SIZE, CHUNK_OVERLAP

def chunk_text(text, chunk_size=CHUNK_SIZE, overlap=CHUNK_OVERLAP):
    words = text.split()
    chunks = []

    start = 0
    while start < len(words):
        end = start + chunk_size
        chunk_words = words[start:end]
        chunks.append(" ".join(chunk_words))
        start += chunk_size - overlap

    return chunks


def chunk_documents():
    docs = load_documents()
    all_chunks = []

    for doc in docs:
        text_chunks = chunk_text(doc["text"])
        for i, chunk in enumerate(text_chunks):
            all_chunks.append({
                "source": doc["filename"],
                "chunk_id": f"{doc['filename']}_{i}",
                "text": chunk
            })

    return all_chunks


if __name__ == "__main__":
    chunks = chunk_documents()
    print(f"Created {len(chunks)} chunks total:")
    for chunk in chunks:
        print(f"- {chunk['chunk_id']} ({len(chunk['text'].split())} words)")