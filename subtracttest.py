import unittest
from calculator import Calculator  

class TestCalculator(unittest.TestCase):
    def setUp(self):
       
        self.calc = Calculator()

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(0, 0), 0)
        self.assertEqual(self.calc.subtract(-2, -3), 1)

if __name__ == "__main__":
    unittest.main()
