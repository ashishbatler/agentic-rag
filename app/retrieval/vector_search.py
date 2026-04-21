from app.core.database import get_connection
from app.embeddings.embedding import get_embedding

def vector_search(query: str, k=3):
    conn = get_connection()
    cur = conn.cursor()

    emb = get_embedding(query)

    cur.execute("""
        SELECT content
        FROM documents
        ORDER BY embedding <=> %s
        LIMIT %s;
    """, (emb, k))

    results = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()
    return results