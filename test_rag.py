from rag.rag_pipeline import RAGPipeline


# PDF path
pdf_path = "documents/hr/leave_policy.pdf"


# Create RAG pipeline
rag = RAGPipeline(pdf_path)


# Ask a question
question = "How many sick leaves are employees allowed?"


answer, sources = rag.ask(question)


print("\nANSWER:")
print(answer)


print("\nSOURCES:")

for source in sources:

    print("Source:", source["source"])
    print("Page:", source["page"])
    print("Text:", source["text"])
    print("-" * 60)