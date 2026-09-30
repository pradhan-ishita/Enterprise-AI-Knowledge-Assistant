from typing import TypedDict
from langgraph.graph import StateGraph, START, END

from agents.manager_agent import manager_router
from agents.sql_agent_runner import run_sql_agent


class AgentState(TypedDict):
    question: str
    route: str
    answer: str


def route_question(state: AgentState):

    result = manager_router({
        "question": state["question"],
        "route": ""
    })

    return {
        "route": result["route"]
    }


def run_sql(state: AgentState):

    result = run_sql_agent(state["question"])

    return {
        "answer": result["answer"]
    }

def run_rag(state: AgentState):

    from agents.rag_agent import generate_rag_answer

    answer = generate_rag_answer(
        state["question"]
    )

    return {
        "answer": answer
    }


def choose_agent(state: AgentState):

    if state["route"] == "sql":
        return "sql"

    return "rag"


graph = StateGraph(AgentState)

graph.add_node("router", route_question)
graph.add_node("sql", run_sql)
graph.add_node("rag", run_rag)

graph.add_edge(START, "router")

graph.add_conditional_edges(
    "router",
    choose_agent,
    {
        "sql": "sql",
        "rag": "rag"
    }
)

graph.add_edge("sql", END)
graph.add_edge("rag", END)

manager_graph = graph.compile()