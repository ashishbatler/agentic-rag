from app.llm.llm import generate_answer

def rewrite_query(query: str):
    return generate_answer(f"Rewrite this for better retrieval: {query}", "")