import unittest
from calculator import multiply

class TestCalculator(unittest.TestCase):
    
    def test_multiply(self):
        self.assertEqual(multiply(3, 5), 15)
        self.assertEqual(multiply(-3, 5), -15)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(2.5, 4), 10.0)
        self.assertEqual(multiply(0.1, 0.2), 0.02)

if __name__ == '__main__':
    unittest.main()
