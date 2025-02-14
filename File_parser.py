# function to parse the data from the files into a list of tuples with integers
def parse_line(line):
        # Remove the parentheses and split the line into parts
        parts = line.strip('()').split(',')
        return list(int(part) for part in parts)
def file_parser(file_path1, file_path2):

    with open(file_path1, 'r') as f1:
        data1 = f1.read().strip()
    with open(file_path2, 'r') as f2:
        data2 = f2.read().strip()
    
    parsed1 = [parse_line(line) for line in data1.split('\n') if line.startswith('(')]
    parsed2 = [parse_line(line) for line in data2.split('\n') if line.startswith('(')]
    
    return parsed1, parsed2



# operation checker
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