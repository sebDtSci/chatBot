import chromadb
print(dir(chromadb))
from chromadb.config import Settings
# from src.rag.document_reader import read_docx
# from transformers import AutoModelForCausalLM, AutoTokenizer
import ollama
print(dir(ollama))
# from ollama.pipeline import Pipeline
# from ollama import Pipeline
from dataBase_gen import generate_embedding
from document_reader import reader

Settings = Settings()
client = chromadb.Client(Settings)
collection = client.create_collection("documents")

# TODO: toujours utiliser le même tokenisateur
# name_model = 'openchat:latest'
# model = ollama.Model(name_model)

documents = reader("data/documents_to_rag")
# print(documents)

for doc in documents:
    # embedding = generate_embedding(doc['content'])
    # collection.add(doc['id'], embedding, doc)
    collection.add(documents=doc["content"],ids=doc["id"])
    
print(collection)
# def generate_response(context, query):
#     pipeline = Pipeline(model)
#     response = pipeline.run(context + "\n\n" + query)
#     return response

def search_documents(query):
    query_embedding = generate_embedding(query)
    results = collection.query(query_embedding, n_results=5)
    return results

def rag_pipeline(query):
    # Recherche de documents pertinents
    results = search_documents(query)
    context = "\n".join([doc['content'] for doc in results])

    # Génération de la réponse avec Ollama
    # response = generate_response(context, query)
    # print(context)
    return context

# Exemple d'utilisation
query = "A quelle vitesse dois je aller pour voyager dans le temps ?"
response = rag_pipeline(query)
print(response)