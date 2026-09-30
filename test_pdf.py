from rag.document_loader import load_pdf


pdf_path = "documents/hr/leave_policy.pdf"

documents = load_pdf(pdf_path)

for document in documents:

    print("SOURCE:", document["source"])
    print("PAGE:", document["page"])
    print("TEXT:")
    print(document["text"])
    print("-" * 50)