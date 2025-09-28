import unittest
from calculator import Calculator  

class TestCalculator(unittest.TestCase):
    def setUp(self):
       
        self.calc = Calculator()

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3, 2), 6)
        self.assertEqual(self.calc.multiply(0, 5), 0)
        self.assertEqual(self.calc.multiply(-3, 2), -6)
        

if __name__ == "__main__":
    unittest.main()
