from src.QuadraticFunction import QuadraticFunction
import pytest

def test_not_a_quadradic_function_exeception():
    with pytest.raises(Exception):
        func = QuadraticFunction(0, 1, 1)

@pytest.mark.parametrize("a, b, c, x, result", [
    (1, -3, 2, 0, 2), (1, -3, 2, 1, 0), (1, -3, 2, 2, 0),
    (1, -2, 1, 0, 1), (1, -2, 1, 1, 0), (1, -2, 1, 2, 1),
    (1, 2, 5, 0, 5), (1, 2, 5, 1, 8), (1, 2, 5, 2, 13)
])
def test_calculate(a, b, c, x, result):
    func = QuadraticFunction(a, b, c)
    assert func.calculate(x) == result

@pytest.mark.parametrize("a, b, c, delta", [
    (1, -3, 2, 1),
    (1, -2, 1, 0),
    (1, 2, 5, -16)
])
def test_delta(a, b, c, delta):
    func = QuadraticFunction(a, b, c)
    assert func.delta() == delta

@pytest.mark.parametrize("a, b, c, roots", [
    (1, -3, 2, [1, 2]),
    (1, -2, 1, [1])
])
def test_roots(a, b, c, roots):
    func = QuadraticFunction(a, b, c)
    assert func.roots() == roots

@pytest.mark.parametrize("a, b, c, a_res, b_res", [
    (1, -3, 2, 2, -3),
    (1, -2, 1, 2, -2),
    (1, 2, 5, 2, 2)
])
def test_derivative(a, b, c, a_res, b_res):
    func = QuadraticFunction(a, b, c)
    derivative = func.derivative()
    assert derivative.a == a_res
    assert derivative.b == b_res