import numpy as np

def matrix_normalization(matrix, axis=None, norm_type='l2'):
    try:
        matrix = np.array(matrix, dtype=float)

        # Invalid: not 2D
        if matrix.ndim != 2:
            return None

        # Invalid axis
        if axis not in (None, 0, 1):
            return None

        if norm_type == 'l1':
            norm = np.sum(np.abs(matrix), axis=axis, keepdims=True)
        elif norm_type == 'l2':
            norm = np.sqrt(np.sum(matrix**2, axis=axis, keepdims=True))
        elif norm_type == 'max':
            norm = np.max(np.abs(matrix), axis=axis, keepdims=True)
        else:
            return None  # invalid norm type

        # Avoid division by zero
        norm[norm == 0] = 1

        return matrix / norm

    except Exception:
        return None