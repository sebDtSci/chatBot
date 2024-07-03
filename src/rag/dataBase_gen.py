from chromadb.utils import embedding_functions

def generate_embedding(text):
    vectorizer = embedding_functions.DefaultEmbeddingFunction()
    return vectorizer(text)

