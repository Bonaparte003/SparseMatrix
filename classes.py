#!/usr/bin/env python3
class SparseMatrix:
    def __init__(self, parsed_data):
        self.data = parsed_data
        self.rows = len(parsed_data)
        self.columns = len(parsed_data[0])
    
    def transpose(self):
        transposed_matrix = []
        for i in range(self.columns):
            transposed_row = []
            for j in range(self.rows):
                transposed_row.append(self.data[j][i])
            transposed_matrix.append(transposed_row)
        return SparseMatrix(transposed_matrix)

class CsrOperator:
    def __init__(self, sparse_matrix):
        self.sparseobject = sparse_matrix
        self.rows = sparse_matrix.rows
        self.columns = sparse_matrix.columns
        self.data = sparse_matrix.data
    
    def zeros_remover(self):
        column_index = []
        row_index = []
        value = []
        for i in range(self.rows):
            for j in range(self.columns):
                if self.data[i][j] != 0:
                    column_index.append(j)
                    row_index.append(i)
                    value.append(self.data[i][j])
        return row_index, column_index, value

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
                row.append(sum(self.matrix1.data[i][k] * self.matrix2.data[k][j] for k in range(self.matrix1.columns)))
            result.append(row)
        return SparseMatrix(result)