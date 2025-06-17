import pytest

def test_addition():
    assert 1 + 1 == 2

@pytest.mark.parametrize("a, b, expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def test_increment(a,b, expected):
    assert a + b == expected
