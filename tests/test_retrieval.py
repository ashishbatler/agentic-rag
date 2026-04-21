from app.retrieval.hybrid import hybrid_search

def test_search():
    results = hybrid_search("insurance claim")
    assert len(results) > 0