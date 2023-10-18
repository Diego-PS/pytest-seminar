from src.LinearFunction import LinearFunction
import pytest

def test_not_a_linear_function_exeception():
    with pytest.raises(Exception):
        func = LinearFunction(0, 1)

@pytest.mark.parametrize("a, b, x, result", [
    (1, 0, 0, 0), (1, 0, 1, 1), (1, 0, 2, 2),
    (2, 1, 0, 1), (2, 1, 1, 3), (2, 1, 2, 5),
    (-1, 1, 1, 0), (-1, 1, 2, -1), (-1, 1, 3, -2)
])
def test_calculate(a, b, x, result):
    func = LinearFunction(a, b)
    assert func.calculate(x) == result

@pytest.mark.parametrize("a, b, root", [
    (1, 0, 0),
    (2, 1, -0.5),
    (-1, 1, 1)
])
def test_root(a, b, root):
    func = LinearFunction(a, b)
    assert func.root() == root