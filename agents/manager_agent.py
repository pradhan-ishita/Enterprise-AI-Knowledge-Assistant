from typing import TypedDict


class AgentState(TypedDict):
    question: str
    route: str


def manager_router(state: AgentState):

    question = state["question"].lower()


    # --------------------------------------------------
    # RAG / DOCUMENT QUESTIONS
    # --------------------------------------------------

    rag_keywords = [
        "leave",
        "leaves",
        "casual leave",
        "sick leave",
        "annual leave",
        "emergency leave",
        "leave policy",
        "leave request",
        "employee portal",
        "hr policy",
        "policy",
        "document"
    ]


    for keyword in rag_keywords:

        if keyword in question:

            return {
                "question": state["question"],
                "route": "rag"
            }


    # --------------------------------------------------
    # SQL / DATABASE QUESTIONS
    # --------------------------------------------------

    sql_keywords = [
        "salary",
        "employee",
        "employees",
        "department",
        "average",
        "highest",
        "lowest",
        "count",
        "how many employees",
        "job title",
        "hired"
    ]


    for keyword in sql_keywords:

        if keyword in question:

            return {
                "question": state["question"],
                "route": "sql"
            }


    # --------------------------------------------------
    # DEFAULT ROUTE
    # --------------------------------------------------

    return {
        "question": state["question"],
        "route": "rag"
    }