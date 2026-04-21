from app.embeddings.embedding import get_embedding
from app.core.database import get_connection

docs = [
    "Insurance claims can be rejected due to missing documents",
    "Claims must be filed within 30 days"
]

conn = get_connection()
cur = conn.cursor()

for d in docs:
    emb = get_embedding(d)
    cur.execute(
        "INSERT INTO documents (content, embedding) VALUES (%s, %s)",
        (d, emb)
    )

conn.commit()
cur.close()
conn.close()