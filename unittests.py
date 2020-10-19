import warmup2
import unittest

class TestFunction(unittest.TestCase):
    def testSum001(self):
        self.assertTrue(warmup2.sum(1, 1), 2)


if __name__ == '__main__':
    unittest.main()