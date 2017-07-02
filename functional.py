def isFalse(obj):
    return not obj

if __name__ == "__main__":
    import unittest

    class UnitTest(unittest.TestCase):
        def isFalse_test(self):
            self.assertEqual(isFalse(0),True)
            self.assertEqual(isFalse(1),False)
            self.assertEqual(isFalse(-1),False)
            self.assertEqual(isFalse(True),False)
            self.assertEqual(isFalse(False),True)
            self.assertEqual(isFalse(None),True)
            self.assertEqual(isFalse(""),True)
            self.assertEqual(isFalse("a"),False)

    unittest.main()

