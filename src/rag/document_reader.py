from docx import Document
import os

def read_docx(file_path):
    documents = []
    for file in os.listdir(file_path):
        if file.endswith(".docx"):
            doc_path = os.path.join(file_path, file)
            doc = Document(doc_path)
            content = "\n".join([para.text for para in doc.paragraphs])
            documents.append({"id": file, "content": content})
    return documents

word_doc = read_docx("data/documents_to_rag")

print(word_doc)


# # Ajouter des documents
# documents = [
#     {"id": "1", "text": "This is the first document."},
#     {"id": "2", "text": "This is the second document."},
#     # Ajoutez autant de documents que nécessaire
# ]

