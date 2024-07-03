from chromadb.utils import embedding_functions
from sklearn.metrics.pairwise import cosine_similarity

def generate_embedding(text):
    vectorizer = embedding_functions.DefaultEmbeddingFunction()
    return vectorizer(text)

def filtre_augmented(query, context):
    best_match = None
    highest_score = 0
    vect_query = generate_embedding(query)
    for doc in context:
        vect_context = generate_embedding(doc)
        score = cosine_similarity([vect_query], [vect_context])[0][0]

        if score > highest_score:
            highest_score = score
            best_match = doc
    context = best_match if best_match else ""
    return context

