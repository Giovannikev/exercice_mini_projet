import numpy as np
from ..utils.markov_utils import stationary_dist

P = np.array([[0.6, 0.3, 0.1],
              [0.2, 0.5, 0.3],
              [0.1, 0.4, 0.5]])

if __name__ == "__main__":
    print(stationary_dist(P))
