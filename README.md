# SIR Epidemic Simulator

A starter project for the Oxford Research Software Engineering course on AI-assisted software development.

## Getting started

This repository contains a specification and instructions for developing a small SIR epidemic simulator using an AI coding agent.

The application is intentionally not implemented yet.

1. Create your own repository using **Use this template**.
2. Open your new repository in GitHub Codespaces.
3. Read `DESIGN.md` and `AGENTS.md`.
4. Follow the course practicals to implement and extend the simulator.

## Running the dashboard

Install the application dependency, then launch the Streamlit dashboard:

```bash
python -m pip install -r requirements.txt
streamlit run app.py
```

Use the sidebar to adjust the population, initial infections, transmission rate,
recovery rate, and simulation duration. The chart shows susceptible, infected,
and recovered populations for each simulated day.

## Repository contents

- `DESIGN.md` — application requirements and scientific assumptions.
- `AGENTS.md` — instructions and boundaries for AI coding agents.
- `app.py` — Streamlit dashboard for the SIR simulator.
- `docker/` — files used in the environments practical.

## Course progression

During the course, you will:

1. Implement a command-line SIR simulator.
2. Explore dependency management and containers.
3. Introduce automated testing and vaccination.
4. Record your changes using Git.
5. Configure GitHub Actions.
6. Delegate a Streamlit dashboard and review its pull request.

## Recovery points

Recovery points are provided in-case you run into issues during the practicals. These are destructive and will **replace** your current work. Use them only if you are stuck and cannot recover your work.

Recovery points are available as branches for the following practicals:
- `recovery/coding`
- `recovery/testing`
- `recovery/dashboard`

For example, to revert to the `recovery/coding` checkpoint, run:
```
git reset --hard
git clean -fd
git switch main
git reset --hard recovery/coding
```

**Instructor note:** Recovery branches should be rebased onto main whenever the main branch is updated.

## Important

This is an educational example, not a validated epidemiological forecasting tool.

The repository will evolve as you complete the practicals.

