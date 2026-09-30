from rag.document_loader import load_pdf
from rag.chunker import chunk_text
from rag.vector_store import VectorStore


# 1. Load PDF
pdf_path = "documents/hr/leave_policy.pdf"

documents = load_pdf(pdf_path)


# 2. Create chunks
chunks = []

for document in documents:

    text_chunks = chunk_text(document["text"])

    for chunk in text_chunks:

        chunks.append({
            "text": chunk,
            "page": document["page"],
            "source": document["source"]
        })


print("Number of chunks:", len(chunks))


# 3. Create FAISS vector store
vector_store = VectorStore()

vector_store.create_index(chunks)


# 4. Search
question = "How many sick leaves are employees allowed?"

results = vector_store.search(question, k=3)


print("\nSEARCH RESULTS\n")

for result in results:

    print("SOURCE:", result["source"])
    print("PAGE:", result["page"])
    print("TEXT:", result["text"])
    print("-" * 60)