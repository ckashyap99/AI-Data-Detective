import fitz  # PyMuPDF
from docx import Document


class DocumentLoader:

    @staticmethod
    def load_document(uploaded_file):

        file_name = uploaded_file.name.lower()

        if file_name.endswith(".pdf"):
            return DocumentLoader._load_pdf(
                uploaded_file
            )

        elif file_name.endswith(".docx"):
            return DocumentLoader._load_docx(
                uploaded_file
            )

        elif file_name.endswith(".txt"):
            return DocumentLoader._load_txt(
                uploaded_file
            )

        else:
            raise ValueError(
                "Unsupported file type."
            )

    @staticmethod
    def _load_pdf(uploaded_file):

        pdf_bytes = uploaded_file.read()

        doc = fitz.open(
            stream=pdf_bytes,
            filetype="pdf"
        )

        text = ""

        for page in doc:
            text += page.get_text()

        doc.close()

        return text

    @staticmethod
    def _load_docx(uploaded_file):

        doc = Document(uploaded_file)

        text = "\n".join(
            [
                para.text
                for para in doc.paragraphs
            ]
        )

        return text

    @staticmethod
    def _load_txt(uploaded_file):

        return uploaded_file.read().decode(
            "utf-8"
        )