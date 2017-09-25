import functional as F
import math
import copy

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

    return [a*x for x in X] if len(shape_X) == 1 \
        else [sca_mul(a, x) for x in X]

