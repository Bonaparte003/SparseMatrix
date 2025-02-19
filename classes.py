#!/usr/bin/env python3
class SparseMatrix:
    def __init__(self, data, rows=None, columns=None):
        self.data = data
        self.rows = rows if rows is not None else len(data)
        self.columns = columns if columns is not None else max(len(row) for row in data)
        self.fill_matrix()

    def fill_matrix(self):
        for row in self.data:
            while len(row) < self.columns:
                row.append(0)
        while len(self.data) < self.rows:
            self.data.append([0] * self.columns)
    
    def transpose(self):
        transposed_matrix = []
        for i in range(self.columns):
            transposed_row = []
            for j in range(self.rows):
                transposed_row.append(self.data[j][i])
            transposed_matrix.append(transposed_row)
        return SparseMatrix(transposed_matrix)


class Operations:
    def __init__(self, matrix1, matrix2, operator):
        self.matrix1 = matrix1
        self.matrix2 = matrix2
        self.operator = operator
    
    def addition(self):
        result = []
        for i in range(self.matrix1.rows):
            row = []
            for j in range(self.matrix1.columns):
                row.append(self.matrix1.data[i][j] + self.matrix2.data[i][j])
            result.append(row)
        return SparseMatrix(result)
    
    
    def subtraction(self):
        result = []
        for i in range(self.matrix1.rows):
            row = []
            for j in range(self.matrix1.columns):
                row.append(self.matrix1.data[i][j] - self.matrix2.data[i][j])
            result.append(row)
        return SparseMatrix(result)
    
    
    def multiplication(self):
        result = []
        for i in range(self.matrix1.rows):
            row = []
            for j in range(self.matrix2.columns):
                element_sum = 0
                for k in range(self.matrix1.columns):
                    element_sum += self.matrix1.data[i][k] * self.matrix2.data[k][j]
                row.append(element_sum)
            result.append(row)
        return SparseMatrix(result)