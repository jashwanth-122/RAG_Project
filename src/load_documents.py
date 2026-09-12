import os
from config import DATA_FOLDER

def load_documents():
    documents = []

    if not os.path.exists(DATA_FOLDER):
        raise FileNotFoundError(f"Data folder not found: {DATA_FOLDER}")

    for filename in os.listdir(DATA_FOLDER):
        if filename.endswith(".txt"):
            file_path = os.path.join(DATA_FOLDER, filename)

            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()

            if not text.strip():
                print(f"Warning: {filename} is empty, skipping.")
                continue

            documents.append({
                "filename": filename,
                "text": text
            })

    return documents


if __name__ == "__main__":
    docs = load_documents()
    print(f"Loaded {len(docs)} documents:")
    for doc in docs:
        print(f"- {doc['filename']} ({len(doc['text'])} characters)")