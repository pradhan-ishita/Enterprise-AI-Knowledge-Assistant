from agents.manager_graph import manager_graph


questions = [
    "Who has the highest salary?",
    "How many sick leaves are allowed?"
]


for question in questions:

    result = manager_graph.invoke({
        "question": question,
        "route": "",
        "answer": ""
    })

    print("\nQuestion:", question)
    print("Answer:", result["answer"])