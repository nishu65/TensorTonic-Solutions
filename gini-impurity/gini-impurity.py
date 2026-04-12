import numpy as np

def gini(y):
    if len(y) == 0:
        return 0.0
    _, counts = np.unique(y, return_counts=True)
    probs = counts / len(y)
    return 1.0 - np.sum(probs ** 2)


def gini_impurity(y_left, y_right):
    """
    Compute weighted Gini impurity for a binary split.
    """
    n_left = len(y_left)
    n_right = len(y_right)
    n_total = n_left + n_right

    # Handle edge case: both empty
    if n_total == 0:
        return 0.0

    gini_left = gini(y_left)
    gini_right = gini(y_right)

    weighted_gini = (n_left / n_total) * gini_left + (n_right / n_total) * gini_right

    return weighted_gini