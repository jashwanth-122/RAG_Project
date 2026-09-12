import os

# -----------------------------
# Shared project settings
# -----------------------------

# folder where this config.py file lives (always src/)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DATA_FOLDER = os.path.join(BASE_DIR, "..", "data")
CHROMA_PATH = os.path.join(BASE_DIR, "..", "outputs", "chroma_db")
COLLECTION_NAME = "project_docs"

EMBEDDING_MODEL_NAME = "all-MiniLM-L6-v2"
CLAUDE_MODEL = "claude-haiku-4-5-20251001"

CHUNK_SIZE = 300
CHUNK_OVERLAP = 50
TOP_K = 3