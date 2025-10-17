import numpy as np

def stationary_dist(P: np.ndarray) -> np.ndarray:
    w, v = np.linalg.eig(P.T)
    i = np.argmin(np.abs(w - 1))
    pi = np.real(v[:, i])
    return pi / np.sum(pi)
