#!/usr/bin/env python3

"""A function that parses a file containing matrices and returns a list of matrices."""
def parse_line(line):
    parts = line.strip('()').split(',')
    return [int(part.strip()) for part in parts]

"""A function that reads two files containing matrices and returns a list of matrices."""
def file_parser(file_path1, file_path2):

    with open(file_path1, 'r') as f1:
        data1 = f1.read().strip()
    with open(file_path2, 'r') as f2:
        data2 = f2.read().strip()
    
    rows1, columns1, rows2, columns2 = None, None, None, None

    for line in data1.split('\n'):
        if 'row' in line or 'rows' in line:
            rows1 = int(line.split('=')[-1].strip())
            break
    for line in data1.split('\n'):
        if 'col' in line or 'cols' in line:
            columns1 = int(line.split('=')[-1].strip())
            break
    for line in data2.split('\n'):
        if 'row' in line or 'rows' in line:
            rows2 = int(line.split('=')[-1].strip())
            break
    for line in data2.split('\n'):
        if 'col' in line or 'cols' in line:
            columns2 = int(line.split('=')[-1].strip())
    

    parsed1 = [parse_line(line) for line in data1.split('\n') if line.startswith('(')]
    parsed2 = [parse_line(line) for line in data2.split('\n') if line.startswith('(')]
    
    return parsed1, rows1, columns1, parsed2, rows2, columns2

'''Operations Checker'''
def operaction_checker(Matrix1, Matrix2, operation):
    if operation == '+':
        if Matrix1.rows != Matrix2.rows or Matrix1.columns != Matrix2.columns:
            return False
        else:
            return True
    elif operation == '-':
        if Matrix1.rows != Matrix2.rows or Matrix1.columns != Matrix2.columns:
            return False
        else:
            return True
    elif operation == '*':
        if Matrix1.columns != Matrix2.rows:
            return False
        else:
            return True
    elif operation == 't':
        return True
    else:
        return False