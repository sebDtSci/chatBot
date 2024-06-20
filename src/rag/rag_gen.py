import chromadb
from chromadb.config import Settings
from src.rag.document_reader import read_docx

Settings = Settings()
client = chromadb.Client(Settings)

