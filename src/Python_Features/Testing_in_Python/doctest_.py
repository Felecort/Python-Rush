import doctest


def power(a, b):
    """
    >>> power(4, 2)
    16
    >>> power(4, 3)
    17
    >>> power(4, 4)
    256
    """
    z = a ** b
    return z


# def foo():
#     """
#     >>> foo()
#     8
#     """
#     return 8


# c = power(4, 2)
doctest.testmod()
