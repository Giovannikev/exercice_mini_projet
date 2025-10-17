import numpy as np
import matplotlib.pyplot as plt

def simulate_mm1(lam=0.8, mu=1.0, N=5000, seed=0, save_figs=False):
    rng = np.random.default_rng(seed)
    inter_arr = rng.exponential(1/lam, N)
    srv_time  = rng.exponential(1/mu, N)
    arrivals = np.cumsum(inter_arr)
    start, finish = np.empty(N), np.empty(N)
    server_free = 0.0
    for i in range(N):
        start[i] = max(arrivals[i], server_free)
        finish[i] = start[i] + srv_time[i]
        server_free = finish[i]
    wait = start - arrivals
    sojourn = finish - arrivals

    # Trajectoire de la longueur du système
    times = np.concatenate([arrivals, finish])
    types = np.concatenate([np.ones(N), -np.ones(N)])
    order = np.argsort(times); times = times[order]; types = types[order]
    q, q_len = [], 0
    for typ in types:
        q_len += 1 if typ == 1 else -1
        q.append(q_len)

    # Graphiques
    plt.figure()
    plt.step(times, q, where='post')
    plt.xlabel("Temps"); plt.ylabel("Nb clients"); plt.title("Trajectoire M/M/1")
    if save_figs: plt.savefig("data/figures/trajectory.png", dpi=150)
    plt.show()

    plt.figure()
    plt.hist(wait, bins=40, density=True)
    plt.xlabel("Attente (W)"); plt.ylabel("Densité"); plt.title("Distribution des attentes")
    if save_figs: plt.savefig("data/figures/wait_hist.png", dpi=150)
    plt.show()

    return wait.mean(), sojourn.mean()

if __name__ == "__main__":
    w, t = simulate_mm1()
    print(f"E[W] ≈ {w:.3f} | E[T] ≈ {t:.3f}")
