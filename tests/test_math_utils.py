import unittest
from operations.math_utils import nth_root

class TestMathUtils(unittest.TestCase):
    def test_nth_root(self):
        self.assertAlmostEqual(nth_root(27, 3), 3.0)
        self.assertAlmostEqual(nth_root(16, 4), 2.0)
        with self.assertRaises(ValueError):
            nth_root(4, 0)
        with self.assertRaises(ValueError):
            nth_root(-16, 2)

if __name__ == "__main__":
    unittest.main()
