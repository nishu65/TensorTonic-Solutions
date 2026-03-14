import numpy as np

def vector_norm_3d(v):
    v = np.asarray(v)

    if v.ndim == 1:  # single vector
        return float(np.sqrt(np.sum(v**2)))
    
    elif v.ndim == 2:  # batch of vectors
        return np.sqrt(np.sum(v**2, axis=1))