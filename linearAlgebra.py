import functional as F
import math
import copy
from sympy import Symbol, pprint, solve

def shape(matrix):
    if not F.is_sequence(matrix): return None

    shapes = []
    acc_matrix = matrix

    while True:
        matrix_length = len(acc_matrix)
        shapes.append(matrix_length)

        if not F.is_sequence(acc_matrix[0]):
            return shapes
        acc_matrix = acc_matrix[0]

def mat_mul(X, Y):
    # 일단 2D 만 가능하도록 구현되어 있음
    # 차원 검사 로직은 추후 적용할 예정

    return [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def mat_add(X, Y):
    shape_X, shape_Y = shape(X), shape(Y)

    if shape_X != shape_Y:
        error_message = "Shape of X and B must be same. X: {}, Y: {}".format(shape_X, shape_Y)
        #raise ValueError(error_message)
        return None

    return [x + y for x, y in zip(X, Y)] if len(shape_X) == 1 \
        else [mat_add(x, y) for x, y in zip(X, Y)]

def sca_mul(a, X):
    shape_X = shape(X)

    return [a * x for x in X] if len(shape_X) == 1 \
        else [sca_mul(a, x) for x in X]

def linear_combination(V, basis):
    len_V = shape(V)[0]
    shape_basis = shape(basis)

    if F.any(shape_basis, lambda b: b != len_V):
        error_message = "Length of V and basis must be same.";
        #raise ValueError(error_message)
        return None

    S = [Symbol('S{}'.format(i)) for i in range(len_V)]
    print(len(S))
    expr = [F.reduce([S[j] * basis[i][j] for j in range(len_V)], lambda x,y: x+y, -V[i]) for i in range(len_V)]
    s = solve(expr, dict=True)[0]
    return [s[S[i]] for i in range(len_V)]

if __name__ == '__main__':
    print(linear_combination([1,2,3],[[1,0,0],[0,1,0],[0,0,1]]))











