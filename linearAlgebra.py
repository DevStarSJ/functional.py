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
    shape_X, shape_Y = shape(X), shape(Y)

    if shape_X[1] != shape_Y[0]:
        error_message = "Shape of X [1] and B [0] must be same. X: {}, Y: {}".format(shape_X, shape_Y)
        #raise ValueError(error_message)
        return None

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
    expr = [F.reduce([S[j] * basis[i][j] for j in range(len_V)], lambda x,y: x+y, -V[i]) for i in range(len_V)]
    solution = solve(expr, dict=True)

    if len(solution) == 0:
        error_message = "There is linear independent basis.";
        #raise ValueError(error_message)
        return []

    s = solution[0]
    return [s[S[i]] for i in range(len_V)]


def is_linear_independent(basis):
    shape_basis = shape(basis)
    V = F.reduce(basis, lambda a,b: mat_add(a,b), [0 for _ in range(0,shape_basis[0])])

    return len(linear_combination(V,basis)) > 0

def determinant(A, x = -1):
    shape_A = shape(A)
    len_A = shape_A[0]

    if len_A != shape_A[1]:
        error_message = "Matrix A must be square matrix : {}".format(shape_A)
        #raise ValueError(error_message)
        return None

    if len_A == 1:
        return A[0][0]

    result = 0

    if x == -1:
        sign = -1
        for i in range(len_A):
            sign *= -1
            result += determinant(A, i) * sign
    else:
        sub_A = []
        for i in range(1, len_A):
            row = [value for i, value in enumerate(A[i]) if i != x]
            sub_A.append(row)
        result = A[0][x] * determinant(sub_A)
    return result


if __name__ == '__main__':
    pass












