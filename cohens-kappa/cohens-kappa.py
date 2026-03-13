import numpy as np

def cohens_kappa(rater1, rater2):
    x = np.array(rater1)
    y = np.array(rater2)

    n = len(x)

    # observed agreement
    po = np.sum(x == y) / n

    labels = np.union1d(x, y)

    pe = 0
    for label in labels:
        px = np.sum(x == label) / n
        py = np.sum(y == label) / n
        pe += px * py

    # avoid division by zero
    if pe == 1:
        return 1.0

    return (po - pe) / (1 - pe)