from app.retrieval.vector_search import vector_search
from app.retrieval.keyword_search import keyword_search

def hybrid_search(query: str):
    vec = vector_search(query)
    key = keyword_search(query)

    combined = list(dict.fromkeys(vec + key))
    return combined[:3]