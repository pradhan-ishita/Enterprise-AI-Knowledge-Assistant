import os

from dotenv import load_dotenv
from groq import Groq

from rag.document_loader import load_pdf
from rag.chunker import chunk_text
from rag.vector_store import VectorStore


# Load environment variables
load_dotenv()


class RAGPipeline:

    def __init__(self, documents_folder):

        self.documents_folder = documents_folder

        # --------------------------------
        # 1. Find all PDF files
        # --------------------------------

        pdf_files = []

        for root, directories, files in os.walk(documents_folder):

            for file in files:

                if file.lower().endswith(".pdf"):

                    pdf_path = os.path.join(root, file)

                    pdf_files.append(pdf_path)

        print(f"Found {len(pdf_files)} PDF files.")

        # --------------------------------
        # 2. Load all PDFs
        # --------------------------------

        documents = []

        for pdf_path in pdf_files:

            print(f"Loading: {pdf_path}")

            pdf_documents = load_pdf(pdf_path)

            documents.extend(pdf_documents)

        # --------------------------------
        # 3. Create chunks
        # --------------------------------

        chunks = []

        for document in documents:

            text_chunks = chunk_text(
                document["text"]
            )

            for chunk in text_chunks:

                chunks.append({
                    "text": chunk,
                    "page": document["page"],
                    "source": document["source"]
                })

        print(f"Created {len(chunks)} chunks.")

        # --------------------------------
        # 4. Create FAISS index
        # --------------------------------

        self.vector_store = VectorStore()

        self.vector_store.create_index(chunks)

        # --------------------------------
        # 5. Create Groq client
        # --------------------------------

        self.client = Groq(
            api_key=os.getenv("GROQ_API_KEY")
        )

        print("RAG Pipeline initialized successfully.")

    def ask(self, question):

        # --------------------------------
        # 6. Retrieve relevant chunks
        # --------------------------------

        results = self.vector_store.search(
            question,
            k=3
        )

        # --------------------------------
        # 7. Combine retrieved context
        # --------------------------------

        context = "\n\n".join(
            result["text"]
            for result in results
        )

        # --------------------------------
        # 8. Create prompt
        # --------------------------------

        prompt = f"""
You are an enterprise knowledge assistant.

Answer the user's question using ONLY the
information provided in the context below.

If the answer is not present in the context,
say:

"I could not find this information in the
provided documents."

Do not make up information.

Context:
{context}

Question:
{question}

Answer:
"""

        # --------------------------------
        # 9. Send request to Groq
        # --------------------------------

        response = self.client.chat.completions.create(

            model="openai/gpt-oss-120b",

            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ]
        )

        answer = response.choices[0].message.content

        return answer, results