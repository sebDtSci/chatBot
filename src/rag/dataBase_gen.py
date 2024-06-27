from chromadb.embedding import Embedding
from chromadb.vectorizer import Vectorizer
import ollama

def generate_embedding(text):
    vectorizer = Vectorizer()
    return vectorizer.vectorize(text)

