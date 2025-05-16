import unittest
from operations import arithmetic

class TestArithmetic(unittest.TestCase):
    def test_is_safe_expression(self):
        self.assertTrue(arithmetic.is_safe_expression("2+3*4"))
        self.assertFalse(arithmetic.is_safe_expression("__import__('os').system('ls')"))
        self.assertFalse(arithmetic.is_safe_expression("a+1"))
        self.assertFalse(arithmetic.is_safe_expression("abs(-1)"))

    def test_nth_root_method(self):
        calc = arithmetic.Calculator()
        self.assertAlmostEqual(calc.nth_root(3, 27), 3.0)
        with self.assertRaises(ValueError):
            calc.nth_root(0, 4)
        with self.assertRaises(ValueError):
            calc.nth_root(2, -4)

if __name__ == "__main__":
    unittest.main()
