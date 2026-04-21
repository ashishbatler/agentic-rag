from sentence_transformers import SentenceTransformer

model = SentenceTransformer("jinaai/jina-embeddings-v2-base-en")

def get_embedding(text: str):
    return model.encode(text).tolist()