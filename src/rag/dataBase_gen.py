from chromadb import Embeddings
# from chromadb import Vectorizer
import ollama

def generate_embedding(text):
    vectorizer = Embeddings()
    return vectorizer.vectorize(text)

