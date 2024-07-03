# from chromadb import Embeddings
from chromadb.utils import embedding_functions
# from chromadb import Vectorizer
import ollama

def generate_embedding(text):
    vectorizer = embedding_functions.DefaultEmbeddingFunction()
    return vectorizer(text)

