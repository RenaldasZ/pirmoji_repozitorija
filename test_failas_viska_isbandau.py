import unittest

class TestAssertMethods(unittest.TestCase):
    def test_assertEqual(self):
        self.assertEqual(3 + 2, 5)

    def test_assertTrue(self):
        self.assertTrue(3 < 5)

    def test_assertFalse(self):
        self.assertFalse(5 < 3)

    def test_assertIs(self):
        a = [1, 2, 3]
        b = a
        self.assertIs(a, b)

    def test_assertIsNone(self):
        self.assertIsNone(None)

if __name__ == '__main__':
    unittest.main()