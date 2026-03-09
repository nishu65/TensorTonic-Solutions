def precision_recall_at_k(recommended, relevant, k):
    """
    Compute precision@k and recall@k for a recommendation list.
    """
    
    recommended_k = recommended[:k]
    
    relevant = set(relevant)
    correct = len(set(recommended_k) & relevant)
    
    precision = correct / k if k > 0 else 0
    recall = correct / len(relevant) if len(relevant) > 0 else 0
    
    return [precision, recall]