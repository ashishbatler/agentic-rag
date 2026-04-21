from app.core.database import get_connection

def keyword_search(query: str, k=3):
    conn = get_connection()
    cur = conn.cursor()

    cur.execute("""
        SELECT content
        FROM documents
        WHERE tsv @@ plainto_tsquery(%s)
        LIMIT %s;
    """, (query, k))

    results = [row[0] for row in cur.fetchall()]

    cur.close()
    conn.close()
    return results