from sentence_transformers import SentenceTransformer
from config import EMBEDDING_MODEL_NAME

_model = None

def get_embedding_model():
    global _model
    if _model is None:
        print("Loading embedding model...")
        _model = SentenceTransformer(EMBEDDING_MODEL_NAME)
    return _model