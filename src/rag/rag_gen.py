import chromadb
from chromadb.config import Settings
from src.rag.document_reader import read_docx
from transformers import AutoModelForCausalLM, AutoTokenizer

Settings = Settings()
client = chromadb.Client(Settings)

# TODO: toujours utiliser le même tokenisateur
name_model = 'openchat:latest'
