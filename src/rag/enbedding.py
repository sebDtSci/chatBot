from chromadb.utils import embedding_functions
from sklearn.metrics.pairwise import cosine_similarity

def generate_embedding(text):
    vectorizer = embedding_functions.DefaultEmbeddingFunction()
    return vectorizer(text)


