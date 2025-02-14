# BX Operator - Advanced Matrix Operations Suite

## Overview

BX Operator is a command-line interface (CLI) tool designed for performing advanced operations on sparse matrices. It supports loading matrices from files, performing various matrix operations, and displaying results in a user-friendly format.


## Features

- **Loading and Displaying Matrices**
  - Load matrices from files
  - Display matrices in a readable format

- **Matrix Operations**
  - Addition, Subtraction, Multiplication
  - Transposition
  - Conversion to Compressed Sparse Row (CSR) format

- **Error Handling**
  - Detailed error messages for file format issues and dimension mismatches

## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/Bonaparte003/SparseMatrix.git
    ```
2. Navigate to the project directory:
    ```sh
    cd BXOperator
    ```
3. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

!Installation

## Usage

1. Start the CLI:
    ```sh
    python main.py
    ```
2. Use the following commands to interact with the tool:
    - `load <file_path1> <file_path2>`: Load two matrices from specified files
    - `show`: Display the loaded matrices
    - `+`: Perform matrix addition
    - `-`: Perform matrix subtraction
    - `*`: Perform matrix multiplication
    - `t`: Transpose the matrix
    - `csr`: Convert the matrix to CSR format
    - `help`: Display the help menu
    - `exit`: Exit the application


## File Format Requirements

- Input files should contain space-separated numbers
- Each line represents a row in the matrix
- All rows must have the same number of columns
- Example format:
    ```
    (1 0 0)
    (0 1 0)
    (0 0 1)
    ```

## Error Handling

- Success indicators show when operations complete
- Error messages explain why operations fail
- Loading errors indicate file format issues
- Dimension mismatch errors show specific requirements

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

## DEMO

![BX Operator](images/1.png)
![Matrix Operations](images/2.png)
![Matrix Addition](images/3.png)
![CLI Usage](images/5.png)
![File Format](images/6.png)
![Error Handling](images/7.png)
