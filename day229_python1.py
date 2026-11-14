import unittest

def multiply(a, b):
    return a * b

class TestMultiply(unittest.TestCase):

    def test_positive(self):
        self.assertEqual(multiply(3, 4), 12)

    def test_negative(self):
        self.assertEqual(multiply(-2, 3), -6)

    def test_zero(self):
        self.assertEqual(multiply(5, 0), 0)

if __name__ == "__main__":
    unittest.main()
