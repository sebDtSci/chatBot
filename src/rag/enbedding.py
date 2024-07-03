from chromadb.utils import embedding_functions
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
from numpy.linalg import norm

def generate_embedding(text):
    vectorizer = embedding_functions.DefaultEmbeddingFunction()
    return vectorizer(text)

def cosine_sim(a, b):
    return np.dot(a, b)/(norm(a)*norm(b))


