import unittest
import functional as F

class UnitTest(unittest.TestCase):
    def test_isFalse(self):
        self.assertEqual(F.isFalse(None),True)
        self.assertEqual(F.isFalse(0),True)
        self.assertEqual(F.isFalse(1),False)
        self.assertEqual(F.isFalse(-1),False)
        self.assertEqual(F.isFalse(True),False)
        self.assertEqual(F.isFalse(False),True)
        self.assertEqual(F.isFalse(""),True)
        self.assertEqual(F.isFalse("a"),False)

if __name__ == "__main__":
    unittest.main()