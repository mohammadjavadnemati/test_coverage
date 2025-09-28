import unittest
from calculator import Calculator  

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(-1, -1), -2)
        self.assertEqual(self.calc.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-2, -3), 1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, 2), -6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        with self.assertRaises(ValueError):
            self.calc.divide(5, 0)

    def test_power(self):
        self.assertEqual(self.calc.power(2, 3), 8)
        self.assertEqual(self.calc.power(5, 0), 1)
        self.assertEqual(self.calc.power(2, -1), 0.5)

    def test_factorial(self):
        self.assertEqual(self.calc.factorial(5), 120)
        self.assertEqual(self.calc.factorial(0), 1)
        with self.assertRaises(ValueError):
            self.calc.factorial(-1)

    def test_sqrt(self):
        self.assertEqual(self.calc.sqrt(16), 4)
        self.assertEqual(self.calc.sqrt(0), 0)
        with self.assertRaises(ValueError):
            self.calc.sqrt(-4)

    def test_sum_of_numbers(self):
        self.assertEqual(self.calc.sum_of_numbers([1, 2, 3]), 6)
        self.assertEqual(self.calc.sum_of_numbers([]), 0)
        with self.assertRaises(ValueError):
            self.calc.sum_of_numbers([1, "a", 3])

    def test_is_prime(self):
        self.assertTrue(self.calc.is_prime(7))
        self.assertFalse(self.calc.is_prime(4))
        self.assertFalse(self.calc.is_prime(1))
        self.assertFalse(self.calc.is_prime(0))
        self.assertFalse(self.calc.is_prime(-3))


if __name__ == "__main__":
    unittest.main()
