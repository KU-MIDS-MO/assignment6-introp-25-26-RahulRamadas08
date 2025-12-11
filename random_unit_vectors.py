import numpy as np

def random_unit_vectors(num_vectors, dim):
    
    M = np.random.randn(num_vectors, dim)
    
    for i in range(num_vectors):
        M[i] /= np.linalg.norm(M[i], ord=2)
    
    return M

print(random_unit_vectors(4, 2))