from agents.sql_agent_runner import run_sql_agent


question = "Who are the top 3 highest-paid employees?"

result = run_sql_agent(question)

print("Success:")
print(result["success"])

print("\nGenerated SQL:")
print(result["sql"])

print("\nDatabase Results:")
for row in result.get("results", []):
    print(row)

print("\nFinal Answer:")
print(result["answer"])