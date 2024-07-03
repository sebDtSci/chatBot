import chromadb
from chromadb.config import Settings
from src.rag.document_reader import reader
from src.rag.dataBase_gen import generate_embedding

# Initialize Chroma
chromadb_client = chromadb.Client(Settings())
collection = chromadb_client.create_collection("documents")

# Add documents
documents = reader("data/documents_to_rag")
collection.add(documents=documents["content"],ids=documents["id"])

def rag_pipeline(query:str) ->str :
    res = collection.query(query_texts=query, n_results=1)
    res = res["documents"]
    context = "".join([j for i in res for j in i])
    return context