import unittest


def foo(a, b):
    return a * 2 + b


class TestMy(unittest.TestCase):
    # False
    def test_1(self):
        z = foo(1, 2)
        self.assertEqual(z, 5)

    # True
    def test_2(self):
        z = foo(4, 8)
        self.assertEqual(z, 16)

    # False
    def test_3(self):
        z = foo(1, 0)
        self.assertEqual(z, 3)


if __name__ == "__main__":
    unittest.main()
