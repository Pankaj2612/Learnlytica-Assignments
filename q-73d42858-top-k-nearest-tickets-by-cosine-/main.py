import numpy as np
def ticket_matrix():
    # Fixed 5x4 matrix of TaskFlow ticket embeddings used by the tests.
    return [[1,0,0,0], [0,1,0,0], [0.9,0.1,0,0], [0,0,1,0], [0.5,0,0.5,0]]

def top_k(matrix, query, k):
    # Return the k rows most similar to query by cosine similarity, best first,
    # as a list of [row_index, rounded_score]. Break ties by smaller index.
    result = []
    for i in range(len(matrix)):
        score = cosine_similarity(matrix[i],query)
        result.append([i,score])
    result.sort(key=lambda t: (-t[1],t[0]))
    k = min(k,len(matrix))
    return result[:k]

def cosine_similarity(a, b):
    a = np.asarray(a,dtype=float)
    b = np.asarray(b,dtype=float)
    denom = np.linalg.norm(a) * np.linalg.norm(b)
    if  denom < 1e-10:
        return 0.0
    return round(np.dot(a,b)/denom,6)
