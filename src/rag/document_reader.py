from docx import Document # python-docx
import fitz  # PyMuPDF
import os

def chunk_text(text, chunk_size=512, overlap=50):
    """
    Chunk the text into segments of specified size with overlap.
    """
    chunks = []
    start = 0
    while start < len(text):
        end = min(start + chunk_size, len(text))
        chunk = text[start:end]
        chunks.append(chunk)
        start += (chunk_size - overlap)
    return chunks

def read_docx(file_path:str) -> list:
    documents = []
    for file in os.listdir(file_path):
        if file.endswith(".docx"):
            doc_path = os.path.join(file_path, file)
            doc = Document(doc_path)
            content = "\n".join([para.text for para in doc.paragraphs])
            chunks = chunk_text(content)
            for i, chunk in enumerate(chunks):
                documents.append({"id": f"{file}_{i}", "content": chunk})
    return documents

def read_txt(file_path:str) -> list:
    documents = []
    for file in os.listdir(file_path):
        if file.endswith(".txt"):
            doc_path:str = os.path.join(file_path, file)
            with open(doc_path, "r") as cont:
                content = cont.read()
            chunks = chunk_text(content)
            for i, chunk in enumerate(chunks):
                documents.append({"id": f"{file}_{i}", "content": chunk})
    return documents
    
def read_pdf(file_path:str) -> list:
    documents = []
    for file in os.listdir(file_path):
        if file.endswith(".pdf"):
            doc_path = os.path.join(file_path, file)
            doc = fitz.open(doc_path)
            content = ""
            for page_num in range(len(doc)):
                page = doc.load_page(page_num)
                content += page.get_text()
            chunks = chunk_text(content)
            for i, chunk in enumerate(chunks):
                documents.append({"id": f"{file}_{i}", "content": chunk})
    return documents

def reader(file_path:str)-> list:
    documents = []
    documents.extend(read_docx(file_path))
    documents.extend(read_txt(file_path))
    documents.extend(read_pdf(file_path))
    return documents

