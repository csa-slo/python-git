import sys
import math

class Matrix:

    def __init__(self, m, n):
        self.m = m
        self.n = n
        self.matrix = [[None for i in range(m)] for j in range(n)]

    def __repr__(self):
        _repr = ''
        for i in range(self.m):
            _repr += '['
            for j in range(self.n):
                _repr += str(self.matrix[j][i])
                if j < self.n - 1:
                    _repr += ', '
            _repr += ']\n'
        return _repr
                
    def row_entry(self):
        for i in range(self.m):
            for j in range(self.n):
                try:
                    self.matrix[j][i] = int(input('Enter entry '+str(i)+', '+str(j)+': '))
                except:
                    self.matrix[j][i] = float(input('Enter entry '+str(i)+', '+str(j)+': '))

    def col_entry(self):
        for j in range(self.n):
            for i in range(self.m):
                try:
                    self.matrix[j][i] = int(input('Enter entry '+str(i)+', '+str(j)+': '))
                except:
                    self.matrix[j][i] = float(input('Enter entry '+str(i)+', '+str(j)+': '))

    def row_replace(self, row1, row2):
        for j in range(self.n):
            temp = self.matrix[j][row1]
            self.matrix[j][row1] = self.matrix[j][row2]
            self.matrix[j][row2] = temp

    def row_scale(self, row, scalar):
        for j in range(self.n):
            self.matrix[j][row] *= scalar

    def row_update(self, row1, row2, scalar):
        for j in range(self.n):
            self.matrix[j][row1] +=  scalar*self.matrix[j][row2]

    def rref(self):
        for pivot in range(self.m):
            entry = False
            nonzero_row = pivot 
            while not entry and nonzero_row < self.m:
                if self.matrix[pivot][nonzero_row] != 0:
                    entry = True
                else:
                    nonzero_row += 1
            if entry:
                if nonzero_row != pivot:
                    self.row_replace(nonzero_row, pivot)
                scalar1 = self.matrix[pivot][pivot]
                for lower in range(pivot+1, self.m):
                    scalar2 = self.matrix[pivot][lower]
                    if scalar2 != 0:
                        scalar3 = -1*scalar2/scalar1
                        self.row_update(lower, pivot, scalar3)
        for pivot in range(self.m-1, -1, -1):
            if self.matrix[pivot][pivot] != 0:
                if self.matrix[pivot][pivot] != 1:
                    self.row_scale(pivot, 1/self.matrix[pivot][pivot])
                for upper in range(pivot-1, -1, -1):
                    scalar = -1*self.matrix[pivot][upper]
                    if scalar != 0:
                        self.row_update(upper, pivot, scalar)

    def row_add(self, other):
        if self.m != other.m or self.n != other.n:
            raise MathError
        for i in range(self.m):
            for j in range(self.n):
                self.matrix[j][i] += other.matrix[j][i]

    def col_add(self, other):
        if self.m != other.m or self.n != other.n:
            raise MathError
        for j in range(self.n):
            for i in range(self.m):
                self.matrix[j][i] += other.matrix[j][i]

def row_add(matrix1, matrix2):
    if matrix1.m != matrix2.m or matrix1.n != matrix2.n:
        raise MathError
    matrix_sum = Matrix(matrix1.m, matrix1.n)
    for i in range(matrix1.m):
        for j in range(matrix2.n):
            matrix_sum.matrix[j][i] = matrix1.matrix[j][i] + matrix2.matrix[j][i] 
    return matrix_sum

def col_add(matrix1, matrix2):
    if matrix1.m != matrix2.m or matrix1.n != matrix2.n:
        raise MathError
    matrix_sum = Matrix(matrix1.m, matrix1.n)
    for j in range(matrix1.n):
        for i in range(matrix1.m):
            matrix_sum.matrix[j][i] = matrix1.matrix[j][i] + matrix2.matrix[j][i]
    return matrix_sum

def row_mult(matrix1, matrix2):
    if matrix1.n != matrix2.m:
        raise MathError
    matrix_product = Matrix(matrix1.m, matrix2.n)
    for i in range(matrix_product.m):
        for j in range(matrix_product.n):
            matrix_product.matrix[j][i] = 0
            for k in range(matrix_product.m):
                matrix_product.matrix[j][i] += matrix1.matrix[k][i]*matrix2.matrix[j][k]
    return matrix_product

def col_mult(matrix1, matrix2):
    if matrix1.n != matrix2.m:
        raise MathError
    matrix_product = Matrix(matrix1.m, matrix2.n)
    for j in range(matrix_product.n):
        for i in range(matrix_product.m):
            matrix_product.matrix[j][i] = 0
            for k in range(matrix_product.m):
                matrix_product.matrix[j][i] += matrix1.matrix[k][i]*matrix2.matrix[j][k]
    return matrix_product
