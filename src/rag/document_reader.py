from docx import Document # python-docx
import fitz  # PyMuPDF
import os

def read_docx(file_path:str)-> list:
    documents = []
    for file in os.listdir(file_path):
        if file.endswith(".docx"):
            doc_path = os.path.join(file_path, file)
            doc = Document(doc_path)
            content = "\n".join([para.text for para in doc.paragraphs])
            documents.append({"id": file, "content": content})
    return documents


def read_txt(file_path:str)-> list:
    documents = []
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            doc_path = os.path.join(file_path, file)
            cont = open(doc_path, "r")
            content = cont.read()
            documents.append({"id": file, "content": content})
    return documents
    
def read_pdf(file_path:str)-> list:
    documents = []
    for file in os.listdir(file_path):
        if file.endswith(".pdf"):
            doc_path = os.path.join(file_path, file)
            doc = fitz.open(doc_path)
            content = ""
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                content += page.get_text()
            documents.append({"id": file, "content": content})
    return documents

def reader(file_path:str)-> list:
    documents = []
    documents.extend(read_docx(file_path))
    documents.extend(read_txt(file_path))
    documents.extend(read_pdf(file_path))
    return documents