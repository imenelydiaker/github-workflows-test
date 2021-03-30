import pytest
from function import Addition


@pytest.fixture(scope="module")
def addition():
    return Addition()


@pytest.mark.parametrize(
    "x, y",
    [
        (1, 2),
    ],
)
def test_addition(x, y):
    res = Addition().add(x, y)
    assert res == 3
