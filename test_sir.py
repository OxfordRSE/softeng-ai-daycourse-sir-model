import pytest
from sir import simulate_sir


def test_population_conservation():
    S, I, R = simulate_sir(1000, 10, 0.3, 0.1, 100)

    for s, i, r in zip(S, I, R):
        assert s + i + r == pytest.approx(1000)


def test_initial_vaccination():
    S, I, R = simulate_sir(
        population=1000,
        infected=10,
        beta=0.3,
        gamma=0.1,
        days=0,
        vaccination=0.2,
    )

    assert S[0] == pytest.approx(792)
    assert I[0] == pytest.approx(10)
    assert R[0] == pytest.approx(198)
