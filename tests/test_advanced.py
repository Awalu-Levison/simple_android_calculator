import unittest
from operations import advanced

class TestAdvanced(unittest.TestCase):
    def test_square(self):
        self.assertEqual(advanced.square("3"), "9.0")
        self.assertEqual(advanced.square("-2"), "4.0")
        self.assertEqual(advanced.square("abc"), "Error")

    def test_square_root(self):
        self.assertEqual(advanced.square_root("9"), "3.0")
        self.assertEqual(advanced.square_root("-1"), "Error")
        self.assertEqual(advanced.square_root("abc"), "Error")

    def test_percentage(self):
        self.assertEqual(advanced.percentage("50"), "0.5")
        self.assertEqual(advanced.percentage("abc"), "Error")

    def test_exponentiate(self):
        self.assertEqual(advanced.exponentiate("2", "3"), "8.0")
        self.assertEqual(advanced.exponentiate("2", "abc"), "Error")

    def test_log_base(self):
        self.assertEqual(advanced.log_base("8", "2"), "3.0")
        self.assertEqual(advanced.log_base("-1", "2"), "Error")

    def test_log10(self):
        self.assertEqual(advanced.log10("100"), "2.0")
        self.assertEqual(advanced.log10("-1"), "Error")

    def test_ln(self):
        self.assertEqual(advanced.ln("1"), "0.0")
        self.assertEqual(advanced.ln("-1"), "Error")

    def test_nth_root(self):
        self.assertEqual(advanced.nth_root("3", "27"), "3.0")
        self.assertEqual(advanced.nth_root("2", "-4"), "Error")
        self.assertEqual(advanced.nth_root("0", "4"), "Error")

if __name__ == "__main__":
    unittest.main()
