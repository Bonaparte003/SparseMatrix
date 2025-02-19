#!/usr/bin/env python3
class SparseMatrix:
    def __init__(self, data, rows=None, columns=None):
        self.data = data
        self.rows = rows if rows is not None else len(data)
        self.columns = columns if columns is not None else max(len(row) for row in data)

    def transpose(self):
        transposed_matrix = []
        for i in range(self.columns):
            transposed_row = []
            for j in range(self.rows):
                if j < len(self.data) and i < len(self.data[j]):
                    transposed_row.append(self.data[j][i])
                else:
                    transposed_row.append(0)
            transposed_matrix.append(transposed_row)
        return SparseMatrix(transposed_matrix, self.columns, self.rows)

    def save_to_file(self, filename):
        with open(filename, 'w') as f:
            f.write(f"rows={self.rows}\n")
            f.write(f"cols={self.columns}\n")
            for row in self.data:
                # Remove trailing zeros
                while row and row[-1] == 0:
                    row.pop()
                if row:
                    f.write(f"({', '.join(map(str, row))})\n")


class Operations:
    def __init__(self, matrix1, matrix2):
        self.matrix1 = matrix1
        self.matrix2 = matrix2

    def addition(self):
        result = []
        for i in range(max(self.matrix1.rows, self.matrix2.rows)):
            row = []
            for j in range(max(self.matrix1.columns, self.matrix2.columns)):
                val1 = self.matrix1.data[i][j] if i < self.matrix1.rows and j < self.matrix1.columns and i < len(self.matrix1.data) and j < len(self.matrix1.data[i]) else 0
                val2 = self.matrix2.data[i][j] if i < self.matrix2.rows and j < self.matrix2.columns and i < len(self.matrix2.data) and j < len(self.matrix2.data[i]) else 0
                row.append(val1 + val2)
            result.append(row)
        return SparseMatrix(result, max(self.matrix1.rows, self.matrix2.rows), max(self.matrix1.columns, self.matrix2.columns))

    def subtraction(self):
        result = []
        for i in range(max(self.matrix1.rows, self.matrix2.rows)):
            row = []
            for j in range(max(self.matrix1.columns, self.matrix2.columns)):
                val1 = self.matrix1.data[i][j] if i < self.matrix1.rows and j < self.matrix1.columns and i < len(self.matrix1.data) and j < len(self.matrix1.data[i]) else 0
                val2 = self.matrix2.data[i][j] if i < self.matrix2.rows and j < self.matrix2.columns and i < len(self.matrix2.data) and j < len(self.matrix2.data[i]) else 0
                row.append(val1 - val2)
            result.append(row)
        return SparseMatrix(result, max(self.matrix1.rows, self.matrix2.rows), max(self.matrix1.columns, self.matrix2.columns))

    def multiplication(self):
        result = []
        for i in range(self.matrix1.rows):
            row = []
            for j in range(self.matrix2.columns):
                element_sum = 0
                for k in range(self.matrix1.columns):
                    val1 = self.matrix1.data[i][k] if i < self.matrix1.rows and k < self.matrix1.columns and i < len(self.matrix1.data) and k < len(self.matrix1.data[i]) else 0
                    val2 = self.matrix2.data[k][j] if k < self.matrix2.rows and j < self.matrix2.columns and k < len(self.matrix2.data) and j < len(self.matrix2.data[k]) else 0
                    element_sum += val1 * val2
                row.append(element_sum)
            result.append(row)
        return SparseMatrix(result, self.matrix1.rows, self.matrix2.columns)