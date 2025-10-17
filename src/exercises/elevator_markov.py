import numpy as np

def elevator_transition_matrix():
    # Etats: (0,↑),(1,↑),(2,↑),(3,↓),(2,↓),(1,↓)
    P = np.array([
        [0,   1,   0,   0,   0,   0],
        [0.1, 0,  0.9,  0,   0,   0],
        [0,   0,   0,  0.9,  0,  0.1],
        [0,   0,   0,   0,   1,   0],
        [0,   0,   0,  0.1,  0,  0.9],
        [0.9, 0,  0.1,  0,   0,   0]
    ])
    return P

if __name__ == "__main__":
    P = elevator_transition_matrix()
    print("P=\n", P)
    print("Stationnaire (uniforme) ~", np.ones(6)/6)
