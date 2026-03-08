import numpy as np

def tanh(x):
    """
    Implement Tanh activation function.
    """
    # Write code here
    x=np.array(x)
    res=[]
    for i in x:
        num=np.exp(i)-np.exp(-i)
        den=np.exp(i)+np.exp(-i)
        res.append(num/den)
    return np.array(res)
    pass