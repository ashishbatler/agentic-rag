from langgraph.graph import StateGraph
from app.retrieval.hybrid import hybrid_search
from app.llm.llm import generate_answer
from app.llm.rewrite import rewrite_query

def search(state):
    return {"docs": hybrid_search(state["query"])}

def grade(state):
    return {"rewrite": len(state["docs"]) == 0}

def rewrite(state):
    return {"query": rewrite_query(state["query"])}

def synthesize(state):
    context = "\n".join(state["docs"])
    return {"answer": generate_answer(state["query"], context)}

graph = StateGraph(dict)

graph.add_node("search", search)
graph.add_node("grade", grade)
graph.add_node("rewrite", rewrite)
graph.add_node("synthesize", synthesize)

graph.set_entry_point("search")

graph.add_edge("search", "grade")
graph.add_conditional_edges(
    "grade",
    lambda x: "rewrite" if x["rewrite"] else "synthesize",
    {"rewrite": "rewrite", "synthesize": "synthesize"}
)
graph.add_edge("rewrite", "search")

app = graph.compile()