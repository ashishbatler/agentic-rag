from fastapi import FastAPI
from app.agent.graph import app

api = FastAPI()

@api.get("/query")
def query(q: str):
    result = app.invoke({"query": q})
    return {"answer": result["answer"]}