from src.mini_project.mm1_queue_sim import simulate_mm1
from src.mini_project.theory import Ew, Et

def main():
    lam, mu = 0.8, 1.0
    ew_sim, et_sim = simulate_mm1(lam, mu, save_figs=True)
    print(f"Simu  : E[W]={ew_sim:.3f}  E[T]={et_sim:.3f}")
    print(f"Théorie: E[W]={Ew(lam,mu):.3f}  E[T]={Et(lam,mu):.3f}")

if __name__ == "__main__":
    main()
