import numpy as np
from os import stat_result

def get_dominant_eigenvalue_and_eigenvector(data, num_steps):
    """
    data: np.ndarray – symmetric diagonalizable real-valued matrix
    num_steps: int – number of power method steps
    
    Returns:
    eigenvalue: float – dominant eigenvalue estimation after `num_steps` steps
    eigenvector: np.ndarray – corresponding eigenvector estimation
    """
    ### YOUR CODE HERE
    start_vec = np.ones(data.shape[1]) / np.sqrt(data.shape[1])
    start_val = start_vec.dot(data.dot(start_vec))
    for i in range(num_steps):
        eigenvector = data.dot(start_vec) / np.linalg.norm(data.dot(start_vec)) 
        eigenvalue = eigenvector.dot(data.dot(eigenvector))
        start_vec = eigenvector
        start_val = eigenvalue

    return float(eigenvalue), eigenvector