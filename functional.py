"""functional utilities
"""


def is_false(arg):
    """Check arg is False.
    It can also be used to return the not value of arg.

    arg: anything
    return: True of False
    """
    return not arg


def is_true(arg):
    """Check arg is True.

    arg: anything
    return: True of False
    """
    return not is_false(arg)


def is_sequence(arg):
    """Check arg is sequence (list, tuple, string)

    arg: anything
    return: True of False
    """
    t = type(arg)
    return t is list or t is tuple or t is str


def is_dict(arg):
    """Check arg is dict

    arg: anything
    return: True of False
    """
    t = type(arg)
    return t is dict


def each(seq, func):
    """Run func for all value of seq

    args:
        seq: sequence or dict
        func: function with one argument 
    return: None
    """
    if (is_false(seq)): return

    if is_sequence(seq):
        [func(x) for x in seq]
    elif is_dict(seq):
        [func(x) for x in seq.values()]


def curry(func):
    """Currying function from left

    args:
        func: function
    return: currying function
    """
    def func_a(*a):
        def func_b(*b):
            return func(*(a+b))
        return func_b
    return func_a


def curryr(func):
    """Currying function from right

    args:
        func: function
    return: currying function
    """
    def func_a(*a):
        def func_b(*b):
            return func(*(b+a))
        return func_b
    return func_a


def map(obj, func):
    if not is_sequence(obj): return []
    _iter = obj
    if is_dict(obj): _iter = obj.values()

    return [func(x) for x in _iter]


def filter(obj, pred):
    if not is_sequence(obj): return []
    _iter = obj
    if is_dict(obj): _iter = obj.values()

    return [x for x in _iter if pred(x)]


def reject(obj, pred):
    return filter(obj, lambda x: not pred(x))


def reduce(obj, func, start):
    if not is_sequence(obj): return None
    acc = start

    def reducer(x):
        nonlocal acc
        acc = func(acc, x)

    each(obj, reducer)
    return acc


def pipe(*args):
    def runner(arg):
        return reduce(list(args), lambda acc, func: func(acc), arg)
    return runner;
