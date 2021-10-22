# import pytest
# pytest.main()
# python -m pytest pytest_.py


def foo(a):
    c = a + 1
    return c


def test_1():
    assert foo(1) == 5


def test_2():
    assert foo(1) == 1


def test_3():
    assert foo(2) == 3


def test_4():
    assert foo(4) == 8
