from app.rag.document_loader import (
    DocumentLoader
)

file_path = "sample.txt"

with open(
    file_path,
    "rb"
) as f:

    text = (
        DocumentLoader._load_txt(f)
    )

print(text[:1000])