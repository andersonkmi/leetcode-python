import warmup2
import unittest
import validparentheses

class TestFunction(unittest.TestCase):
    def testCaseEmptyString(self):
        self.assertTrue(validparentheses.is_valid(''))

    def testInvalidCase001(self):
        self.assertFalse(validparentheses.is_valid('('))


if __name__ == '__main__':
    unittest.main()