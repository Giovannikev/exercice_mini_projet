from src.exercises.elevator_markov import elevator_transition_matrix
from src.exercises.stationary_3states import P as P3
from src.exercises.weather_30days import simulate_weather
from src.utils.markov_utils import stationary_dist

def main():
    print("=== Exo 1 : Ascenseur ===")
    print(elevator_transition_matrix())

    print("\n=== Exo 2 : Stationnaire 3 états ===")
    print(stationary_dist(P3))

    print("\n=== Exo 3 : Météo 30 jours ===")
    _, prop = simulate_weather()
    print(f"Proportion pluie : {prop:.2%}")

if __name__ == "__main__":
    main()
