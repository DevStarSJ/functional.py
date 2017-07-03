"""test run
"""

def fun(*args):
    print(args)

fun(1,2,3,4,5)

def add(a,b,c):
    return a+b+c

p = (1,2,3)
q = (5,6,7)
print(p+q)

#print(type(*p))

print(add(*p))

print(add.__code__.co_argcount)

def curry(func):
    len_func = func.__code__.co_argcount
    def func_a(*a):
        len_a = len(a)
        def func_b(*b):
            return func(*(a+b))
        return func_b
    return func_a

a1 = curry(add)(1,2)
print(a1(4))
a2 = curry(add)(2)
print(a2(4,6))