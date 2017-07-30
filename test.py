"""unittest
"""

import unittest
import functional as F
import mathExt as M

_list = [1,2,3,4]
_tuple = (1,2,3)
_str = "seokjoon.yun"
_dict = { "id": 1, "name": "seokjoon.yun" }
_dict_values = [1, "seokjoon.yun"]
_dict_keys = ["id", "name"]
_matrix = [[1,2],[3,4]]


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

        # _l = []
        # F.each(_dict, lambda x: _l.append(x))
        # self.assertEqual(_dict_values,_l)

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

    def test_map(self):
        self.assertEqual(F.map(_list, lambda x: x*x),[1,4,9,16])
        self.assertEqual(F.map(_tuple, lambda x: x*x),[1,4,9])

    def test_filter(self):
        self.assertEqual(F.filter(_list,lambda x:x % 2 ==0), [2,4])

    def test_reject(self):
        self.assertEqual(F.reject(_list,lambda x:x % 2 ==0), [1,3])

    def test_reduce(self):
        self.assertEqual(F.reduce(_list, lambda x,y:x+y,0),10)

    def test_pipe(self):
        func_pipe = F.pipe(F.curryr(F.map)(lambda x: x+1),F.curryr(F.map)(lambda x: x*2))
        self.assertEqual(func_pipe(_list), [4, 6, 8, 10])

    def test_go(self):
        result = F.go(_list,F.curryr(F.map)(lambda x: x + 1), F.curryr(F.map)(lambda x: x * 2))
        self.assertEqual(result, [4, 6, 8, 10])

    def test_mathExt_shape(self):
        self.assertEqual(M.shape(_list), None)
        self.assertEquals(M.shape(_matrix), [2, 2])

    def test_functional_all(self):
        self.assertEqual(F.all(_list, lambda x: x < 5), True)
        self.assertEqual(F.all(_list, lambda x: x < 2), False)

    def test_functional_any(self):
        self.assertEqual(F.any(_list, lambda x: x < 5), True)
        self.assertEqual(F.any(_list, lambda x: x < 2), True)
        self.assertEqual(F.any(_list, lambda x: x > 5), False)

    def test_mathExt_divisors(self):
        self.assertEqual(M.divisors(28), [1, 2, 4, 7, 14, 28])
        self.assertEquals(M.divisors(21), [1, 3, 7, 21])

    def test_mathExt_sum(self):
        self.assertEqual(M.sum(_list), 10)
        self.assertEqual(M.sum(_tuple), 6)

    def test_mathExt_triangular_number(self):
        self.assertEqual(M.triangular_number(10), 55)
        self.assertEqual(M.triangular_number(1), 1)

if __name__ == "__main__":
    unittest.main()