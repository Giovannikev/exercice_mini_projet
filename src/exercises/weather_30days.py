import numpy as np

def simulate_weather(n=30, seed=42):
    P = np.array([[0.8, 0.2],   # S -> (S,P)
                  [0.4, 0.6]])  # P -> (S,P)
    rng = np.random.default_rng(seed)
    states = np.zeros(n, dtype=int)   # 0=S, 1=P
    states[0] = rng.integers(0, 2)
    for t in range(1, n):
        states[t] = rng.choice([0,1], p=P[states[t-1]])
    prop_pluie = np.mean(states == 1)
    return states, prop_pluie

if __name__ == "__main__":
    _, p = simulate_weather()
    print(f"Proportion de jours de pluie : {p:.2%}")
