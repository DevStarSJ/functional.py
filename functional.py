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
        for i in seq:
            func(i)
    elif is_dict(seq):
        for i in seq.values():
            func(i)

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