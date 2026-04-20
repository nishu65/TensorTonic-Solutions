import numpy as np

def covariance_matrix(X):
    """
    Compute covariance matrix from dataset X.
    """
    X = np.array(X)
    
    # Handle invalid input
    if X.ndim != 2:
        return None
    
    n = X.shape[0]
    if n <= 1:
        return None
    
    mean = np.mean(X, axis=0)
    xc = X - mean
    
    cov = (xc.T @ xc) / (n - 1)   # matrix multiplication
    
    return cov