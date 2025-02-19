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
        row_index = []
        column_index = []
        value = []
        for i in range(self.rows):
            for j in range(self.columns):
                if self.data[i][j] != 0:
                    row_index.append(i)
                    column_index.append(j)
                    value.append(self.data[i][j])
        return row_index, column_index, value
    
    def from_csr(self, row_index, column_index, value):
        max_row = max(row_index) + 1
        max_col = max(column_index) + 1
        matrix = [[0 for _ in range(max_col)] for _ in range(max_row)]
        for r, c, v in zip(row_index, column_index, value):
            matrix[r][c] = v
        return matrix

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
    
    def csr_addition(self, row_index1, column_index1, value1, row_index2, column_index2, value2):
        result_row_index = []
        result_column_index = []
        result_value = []
        
        i, j = 0, 0
        while i < len(row_index1) and j < len(row_index2):
            if row_index1[i] == row_index2[j] and column_index1[i] == column_index2[j]:
                result_row_index.append(row_index1[i])
                result_column_index.append(column_index1[i])
                result_value.append(value1[i] + value2[j])
                i += 1
                j += 1
            elif (row_index1[i] < row_index2[j]) or (row_index1[i] == row_index2[j] and column_index1[i] < column_index2[j]):
                result_row_index.append(row_index1[i])
                result_column_index.append(column_index1[i])
                result_value.append(value1[i])
                i += 1
            else:
                result_row_index.append(row_index2[j])
                result_column_index.append(column_index2[j])
                result_value.append(value2[j])
                j += 1
        
        while i < len(row_index1):
            result_row_index.append(row_index1[i])
            result_column_index.append(column_index1[i])
            result_value.append(value1[i])
            i += 1
        
        while j < len(row_index2):
            result_row_index.append(row_index2[j])
            result_column_index.append(column_index2[j])
            result_value.append(value2[j])
            j += 1
        
        return result_row_index, result_column_index, result_value
    
    def subtraction(self):
        result = []
        for i in range(self.matrix1.rows):
            row = []
            for j in range(self.matrix1.columns):
                row.append(self.matrix1.data[i][j] - self.matrix2.data[i][j])
            result.append(row)
        return SparseMatrix(result)
    
    def csr_subtraction(self, row_index1, column_index1, value1, row_index2, column_index2, value2):
        result_row_index = []
        result_column_index = []
        result_value = []
        
        i, j = 0, 0
        while i < len(row_index1) and j < len(row_index2):
            if row_index1[i] == row_index2[j] and column_index1[i] == column_index2[j]:
                result_row_index.append(row_index1[i])
                result_column_index.append(column_index1[i])
                result_value.append(value1[i] - value2[j])
                i += 1
                j += 1
            elif (row_index1[i] < row_index2[j]) or (row_index1[i] == row_index2[j] and column_index1[i] < column_index2[j]):
                result_row_index.append(row_index1[i])
                result_column_index.append(column_index1[i])
                result_value.append(value1[i])
                i += 1
            else:
                result_row_index.append(row_index2[j])
                result_column_index.append(column_index2[j])
                result_value.append(-value2[j])
                j += 1
        
        while i < len(row_index1):
            result_row_index.append(row_index1[i])
            result_column_index.append(column_index1[i])
            result_value.append(value1[i])
            i += 1
        
        while j < len(row_index2):
            result_row_index.append(row_index2[j])
            result_column_index.append(column_index2[j])
            result_value.append(-value2[j])
            j += 1
        
        return result_row_index, result_column_index, result_value
    
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
    
    def csr_multiplication(self, row_index1, column_index1, value1, row_index2, column_index2, value2):
        result_row_index = []
        result_column_index = []
        result_value = []
        
        for i in range(len(row_index1)):
            for j in range(len(row_index2)):
                if column_index1[i] == row_index2[j]:
                    result_row_index.append(row_index1[i])
                    result_column_index.append(column_index2[j])
                    result_value.append(value1[i] * value2[j])
        
        return result_row_index, result_column_index, result_value