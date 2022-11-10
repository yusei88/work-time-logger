import unittest
import util

class TestFunc(unittest.TestCase):
    def test_addWorkTime(self):
        timeA = "10:45"
        timeB = "1:30"
        expected = "12:15"
        actual = util.addWorkTime(timeA, timeB)
        self.assertEqual(expected, actual)
    
    def test_calcOverTime(self):
        timeA = "18:17"
        expected = "0:17"
        acutual = util.calcOverTime(timeA)
        self.assertEqual(expected, acutual)

if __name__ == "__main__":
    unittest.main()