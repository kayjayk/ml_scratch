import numpy as np

def n_size_ndarray_creation(n, dtype=np.int):
    X = np.arange(0, n**2).reshape(n,n)
    return X


def zero_or_one_or_empty_ndarray(shape, type=0, dtype=np.int):
    X = None

    if type == 0:
        X = np.zeros(shape=shape, dtype=dtype)

    elif type == 1:
        X = np.ones(shape=shape, dtype=dtype)

    else:
        X = np.empty(shape=shape, dtype=dtype)

    return X


def change_shape_of_ndarray(X, n_row):
    res = None
    if n_row == 1:
        res = X.reshape(-1)
    else:
        res = X.reshape(n_row, -1)
    return res

def concat_ndarray(X_1, X_2, axis):
    if X_1.ndim == 1:
        X_1 = X_1.reshape(1, -1)
    if X_2.ndim == 1:
        X_2 = X_2.reshape(1, -1)
    try:
        X = np.concatenate((X_1, X_2), axis = axis)
    except:
        return False
    return X


def normalize_ndarray(X, axis=99, dtype=np.float32):
    res = None
    if axis == 99:
        res = (X - X.mean()) / X.std()
    else:
        if axis:
            X = X.T
            res = ((X - X.mean(axis=0)) / X.std(axis=0)).T

        else:
            res = (X - X.mean(axis=0)) / X.std(axis=0)

    return res


def save_ndarray(X, filename="test.npy"):
    np.savetxt(X, filename)
    pass


def boolean_index(X, condition):
    return np.where(eval("X" + condition))


def find_nearest_value(X, target_value):
    X = X - target_value
    return X[np.abs(X) == np.abs(X).min()] + target_value


def get_n_largest_values(X, n):
    return sorted(X, reverse=True)[:n]
