import math

import functional as F

def shape(matrix):
    if not F.is_sequence(matrix): return None

    len1 = len(matrix)
    if not (len1 > 0 and F.is_sequence(matrix[0])): return None

    len2 = len(matrix[0])

    return [len1, len2]

def matmul(X, Y):
    return [[sum(a*b for a, b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]

def sigmoid(z):
    return 1 / (1 + math.e ** -z)

A = [[1,2],[3,4]]
B = [[5,6],[7,8]]

print(matmul(A,B))