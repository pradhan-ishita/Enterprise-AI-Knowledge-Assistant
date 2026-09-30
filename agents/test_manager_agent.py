from agents.manager_agent import manager_router


questions = [
    "Who has the highest salary?",
    "What is the average salary in Engineering?",
    "How many sick leaves are allowed?",
    "What is the leave request policy?"
]


for question in questions:

    state = {
        "question": question,
        "route": ""
    }

    result = manager_router(state)

    print("\nQuestion:", question)
    print("Route:", result["route"])