from agents.rag_agent import generate_rag_answer


question = "How many sick leaves are employees allowed?"

answer = generate_rag_answer(question)

print("Question:")
print(question)

print("\nRAG Answer:")
print(answer)