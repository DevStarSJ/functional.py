"""unittest
"""

import unittest
import functional as F

_list = [1,2,3,4]
_tuple = (1,2,3)
_str = "seokjoon.yun"
_dict = { "id": 1, "name": "seokjoon.yun" }
_dict_values = [1, "seokjoon.yun"]
_dict_keys = ["id", "name"]

def add(a,b,c): return a+b+c
def sub(a,b,c): return a-b-c

class Class1:
    def __init__(self):
        pass

_class = Class1()

class UnitTest(unittest.TestCase):
    def test_is_false(self):
        self.assertEqual(F.is_false(None),True)
        self.assertEqual(F.is_false(0),True)
        self.assertEqual(F.is_false(1),False)
        self.assertEqual(F.is_false(-1),False)
        self.assertEqual(F.is_false(True),False)
        self.assertEqual(F.is_false(False),True)
        self.assertEqual(F.is_false(""),True)
        self.assertEqual(F.is_false("a"),False)

    def test_is_true(self):
        self.assertEqual(F.is_true(None),False)
        self.assertEqual(F.is_true(0),False)
        self.assertEqual(F.is_true(1),True)
        self.assertEqual(F.is_true(-1),True)
        self.assertEqual(F.is_true(True),True)
        self.assertEqual(F.is_true(False),False)
        self.assertEqual(F.is_true(""),False)
        self.assertEqual(F.is_true("a"),True)

    def test_is_sequence(self):
        self.assertEqual(F.is_sequence(_list),True)
        self.assertEqual(F.is_sequence(_tuple),True)
        self.assertEqual(F.is_sequence(_str),True)
        self.assertEqual(F.is_sequence(_dict),False)
        self.assertEqual(F.is_sequence(_class),False)

    def test_is_dict(self):
        self.assertEqual(F.is_dict(_list),False)
        self.assertEqual(F.is_dict(_tuple),False)
        self.assertEqual(F.is_dict(_str),False)
        self.assertEqual(F.is_dict(_dict),True)
        self.assertEqual(F.is_dict(_class),False)

    def test_each(self):
        self.assertEqual(F.is_dict(_list),False)
        self.assertEqual(F.is_dict(_tuple),False)

        _l = []
        F.each(_list, lambda x: _l.append(x))
        self.assertEqual(_list,_l)

        _l = []
        F.each(_tuple, lambda x: _l.append(x))
        self.assertEqual(list(_tuple),_l)

        _l = []
        F.each(_str, lambda x: _l.append(x))
        self.assertEqual(list(_str),_l)

        _l = []
        F.each(_dict, lambda x: _l.append(x))
        self.assertEqual(_dict_values,_l)

    def test_curry(self):
        a1 = F.curry(add)(1)
        self.assertEqual(a1(2,3),6)
        a2 = F.curry(a1)(3)
        self.assertEqual(a2(4), 8)
        a3 = F.curry(add)(1,1)
        self.assertEqual(a3(1),3)

    def test_curryr(self):
        s1 = F.curryr(sub)(1)
        self.assertEqual(s1(3,2),0)
        s2 = F.curryr(s1)(3)
        self.assertEqual(s2(4), 0)
        s3 = F.curryr(sub)(1,1)
        self.assertEqual(s3(3),1)
    
        
if __name__ == "__main__":
    unittest.main()