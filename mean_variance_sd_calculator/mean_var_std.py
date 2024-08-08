import numpy as np

def calculate(list):
    # Check if input list had exactly 9 numbers. If not, `ValueError.`
    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")

    # Else, convert the list into a 3x3 numpy array
    matrix = np.array(list).reshape(3, 3)

    # Then, we calculate the mean, variance, std, max, min and sum
    # for each row(axis 0), col(axis 1), and entire array(flattened)
    calculations = {
        'mean': [
            matrix.mean(axis=0).tolist(),
            matrix.mean(axis=1).tolist(),
            matrix.mean().tolist()
        ],
        'variance': [
            matrix.var(axis=0).tolist(),
            matrix.var(axis=1).tolist(),
            matrix.var().tolist()
        ],
        'standard deviation': [
            matrix.std(axis=0).tolist(),
            matrix.std(axis=1).tolist(),
            matrix.std().tolist()
        ],
        'max': [
            matrix.max(axis=0).tolist(),
            matrix.max(axis=1).tolist(),
            matrix.max().tolist()
        ],
        'min': [
            matrix.min(axis=0).tolist(),
            matrix.min(axis=1).tolist(),
            matrix.min().tolist()
        ],
        'sum': [
            matrix.sum(axis=0).tolist(),
            matrix.sum(axis=1).tolist(),
            matrix.sum().tolist()
        ]
    }

    return calculations