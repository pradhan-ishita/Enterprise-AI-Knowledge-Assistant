from agents.sql_answer import generate_answer


question = "Who are the top 3 highest-paid employees?"

results = [
    {
        "employee_id": 3,
        "name": "Rohan Das",
        "salary": 95000
    },
    {
        "employee_id": 9,
        "name": "Arjun Kapoor",
        "salary": 90000
    },
    {
        "employee_id": 6,
        "name": "Sneha Roy",
        "salary": 88000
    }
]


answer = generate_answer(question, results)

print("Final Answer:")
print(answer)