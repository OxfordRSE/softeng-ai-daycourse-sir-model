"""Streamlit dashboard for exploring the SIR simulator."""

import streamlit as st

from sir import simulate_sir

st.set_page_config(page_title="SIR Epidemic Simulator", page_icon=":chart_with_upwards_trend:")
st.title("SIR Epidemic Simulator")
st.caption("Explore a simplified deterministic model of a closed population.")

with st.sidebar:
    st.header("Simulation parameters")
    population = st.number_input(
        "Population", min_value=1.0, value=1000.0, step=100.0
    )
    infected = st.number_input(
        "Initial infected", min_value=0.0, value=10.0, step=1.0
    )
    beta = st.number_input(
        "Transmission rate (beta)",
        min_value=0.0,
        max_value=1.0,
        value=0.3,
        step=0.01,
    )
    gamma = st.number_input(
        "Recovery rate (gamma)",
        min_value=0.0,
        max_value=1.0,
        value=0.1,
        step=0.01,
    )
    days = st.number_input("Days", min_value=0, value=100, step=1)

try:
    susceptible, infected_values, recovered = simulate_sir(
        population, infected, beta, gamma, days
    )
except ValueError as error:
    st.error(str(error))
else:
    peak_day = max(range(len(infected_values)), key=infected_values.__getitem__)
    st.metric("Peak infected population", f"{infected_values[peak_day]:.2f}")
    st.caption(f"Peak occurs on day {peak_day}.")
    st.line_chart(
        {
            "Day": range(days + 1),
            "Susceptible": susceptible,
            "Infected": infected_values,
            "Recovered": recovered,
        },
        x="Day",
        y=["Susceptible", "Infected", "Recovered"],
    )
