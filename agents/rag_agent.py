import os

from dotenv import load_dotenv
from groq import Groq

from rag.document_loader import load_pdf
from rag.chunker import chunk_text
from rag.vector_store import VectorStore


load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def build_vector_store():

    pdf_path = "documents/hr/leave_policy.pdf"

    pages = load_pdf(pdf_path)

    documents = []

    for page in pages:

        chunks = chunk_text(page["text"])

        for chunk in chunks:

            documents.append({
                "text": chunk,
                "page": page["page"],
                "source": page["source"]
            })

    vector_store = VectorStore()

    vector_store.create_index(documents)

    return vector_store


def generate_rag_answer(question):

    vector_store = build_vector_store()

    results = vector_store.search(
        question,
        k=3
    )

    print("\nRetrieved Documents:")

    for result in results:
        print("--------------------")
        print("Page:", result["page"])
        print("Text:")
        print(result["text"])

    context = "\n\n".join(
        result["text"]
        for result in results
    )

    prompt = f"""
You are an enterprise AI assistant.

Answer the user's question using ONLY the provided document context.

Document context:
{context}

User question:
{question}

Rules:
1. Do not invent information.
2. If the answer is not present in the context, say that the information was not found in the provided documents.
3. Give a clear and concise answer.
"""

    response = client.chat.completions.create(
        model="openai/gpt-oss-120b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0
    )

    return response.choices[0].message.content.strip()