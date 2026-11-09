"""Deterministic daily SIR simulator for an educational closed-population model."""

import argparse
import math


def simulate_sir(population, infected, beta, gamma, days, vaccination=0.0):
    """Return daily susceptible, infected, and recovered populations."""
    for name, value in (
        ("population", population),
        ("infected", infected),
        ("beta", beta),
        ("gamma", gamma),
        ("vaccination", vaccination),
    ):
        if isinstance(value, bool) or not isinstance(value, (int, float)):
            raise ValueError(f"{name} must be a finite number")
        if isinstance(value, float) and not math.isfinite(value):
            raise ValueError(f"{name} must be a finite number")

    if population <= 0:
        raise ValueError("population must be positive")
    if not 0 <= infected <= population:
        raise ValueError("infected must be between 0 and population")
    if not 0 <= beta <= 1:
        raise ValueError("beta must be between 0 and 1")
    if not 0 <= gamma <= 1:
        raise ValueError("gamma must be between 0 and 1")
    if not 0 <= vaccination <= 1:
        raise ValueError("vaccination must be between 0 and 1")
    if isinstance(days, bool) or not isinstance(days, int) or days < 0:
        raise ValueError("days must be a non-negative integer")

    initial_susceptible = population - infected
    vaccinated = initial_susceptible * vaccination
    susceptible = [initial_susceptible - vaccinated]
    infected_values = [infected]
    recovered = [vaccinated]

    for _ in range(days):
        previous_susceptible = susceptible[-1]
        previous_infected = infected_values[-1]
        previous_recovered = recovered[-1]

        new_infections = beta * previous_susceptible * previous_infected / population
        new_recoveries = gamma * previous_infected

        susceptible.append(previous_susceptible - new_infections)
        infected_values.append(previous_infected + new_infections - new_recoveries)
        recovered.append(previous_recovered + new_recoveries)

    return susceptible, infected_values, recovered


def main():
    parser = argparse.ArgumentParser(
        description="Simulate a deterministic SIR epidemic."
    )
    parser.add_argument("--population", type=float, default=1000)
    parser.add_argument("--infected", type=float, default=10)
    parser.add_argument("--beta", type=float, default=0.3)
    parser.add_argument("--gamma", type=float, default=0.1)
    parser.add_argument("--days", type=int, default=100)
    args = parser.parse_args()

    try:
        susceptible, infected, recovered = simulate_sir(
            args.population, args.infected, args.beta, args.gamma, args.days
        )
    except ValueError as error:
        parser.error(str(error))

    peak_day = max(range(len(infected)), key=infected.__getitem__)
    print("Simulation parameters:")
    print(f"  Population: {args.population:g}")
    print(f"  Initial infected: {args.infected:g}")
    print(f"  Transmission rate (beta): {args.beta:g}")
    print(f"  Recovery rate (gamma): {args.gamma:g}")
    print(f"  Days: {args.days}")
    print(f"Peak infected population: {infected[peak_day]:.2f} on day {peak_day}")
    print("Final populations:")
    print(f"  Susceptible: {susceptible[-1]:.2f}")
    print(f"  Infected: {infected[-1]:.2f}")
    print(f"  Recovered: {recovered[-1]:.2f}")


if __name__ == "__main__":
    main()
