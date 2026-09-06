import pytest
from lesson1 import add, substract, multiply, devide

def test_add():
    assert add(10, 5) == 15

def test_substract():
    assert substract(10, 5) == 5

def test_multiply():
    assert multiply(10, 5) == 50

def test_devide():
    assert devide(10, 5) == 2

def test_devide_by_zero():
    with pytest.raises(ZeroDivisionError):
        devide(10, 0)



# assert add(10, 5) == 15
# assert substract(10, 5) == 5
# assert multiply(10, 5) == 50
# assert devide(10, 5) == 2

# print("All tests passed!")