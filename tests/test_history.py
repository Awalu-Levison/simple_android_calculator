import unittest
from operations.history import HistoryManager

class TestHistoryManager(unittest.TestCase):
    def test_add_and_get_history(self):
        hm = HistoryManager()
        for i in range(7):
            hm.add_entry(f"calc {i}")
        history = hm.get_history()
        self.assertEqual(len(history.splitlines()), 5)
        self.assertTrue("calc 6" in history)
        self.assertFalse("calc 0" in history)

    def test_clear_history(self):
        hm = HistoryManager()
        hm.add_entry("test")
        hm.clear_history()
        self.assertEqual(hm.get_history(), "")

if __name__ == "__main__":
    unittest.main()
