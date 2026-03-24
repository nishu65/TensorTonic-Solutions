import numpy as np

def adagrad_step(w, g, G, lr=0.01, eps=1e-8):
    # Ensure numpy arrays (important for vectorization)
    w = np.array(w)
    g = np.array(g)
    G = np.array(G)
    
    # Step 1: Accumulate squared gradients
    new_G = G + g**2
    
    # Step 2: Update parameters
    new_w = w - (lr / (np.sqrt(new_G+eps) )) * g
    
    return new_w, new_G