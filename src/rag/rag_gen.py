import chromadb
from chromadb.config import Settings
# from src.rag.document_reader import read_docx
# from transformers import AutoModelForCausalLM, AutoTokenizer
import ollama
from ollama.pipeline import Pipeline

Settings = Settings()
client = chromadb.Client(Settings)
collection = client.create_collection("documents")

# TODO: toujours utiliser le même tokenisateur
name_model = 'openchat:latest'
model = ollama.Model(name_model)


for doc in documents:
    embedding = generate_embedding(doc['text'])
    collection.add(doc['id'], embedding, doc)
    
    
def generate_response(context, query):
    pipeline = Pipeline(model)
    response = pipeline.run(context + "\n\n" + query)
    return response

def search_documents(query):
    query_embedding = generate_embedding(query)
    results = collection.query(query_embedding, top_k=5)
    return results

def rag_pipeline(query):
    # Recherche de documents pertinents
    results = search_documents(query)
    context = "\n".join([doc['text'] for doc in results])

    # Génération de la réponse avec Ollama
    response = generate_response(context, query)
    return response

# Exemple d'utilisation
query = "What is the first document about?"
response = rag_pipeline(query)
print(response)