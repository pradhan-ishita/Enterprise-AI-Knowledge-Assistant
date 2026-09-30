from pypdf import PdfReader


def load_pdf(file_path):

    reader = PdfReader(file_path)

    documents = []

    for page_number, page in enumerate(reader.pages):

        text = page.extract_text()

        if text:

            # Clean unnecessary spaces and line breaks
            cleaned_text = " ".join(text.split())

            documents.append({
                "text": cleaned_text,
                "page": page_number + 1,
                "source": file_path
            })

    return documents