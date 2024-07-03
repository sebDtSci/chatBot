import chromadb
from chromadb.config import Settings

from document_reader import reader

chromadb_client = chromadb.Client(Settings())

collection = chromadb_client.create_collection("documents")

documents = reader("data/documents_to_rag")
for doc in documents:
    collection.add(documents=doc["content"],ids=doc["id"])

res = collection.query(query_texts="A quelle vitesse dois je aller pour voyager dans le temps ?", n_results=1)
print(res)
print(res["documents"])

def rag_pipeline(query:str) ->str :
    return collection.query(query_texts=query["documents"], n_results=1)