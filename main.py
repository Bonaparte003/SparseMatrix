from File_parser import file_parser, operaction_checker
from classes import SparseMatrix, Operations
import sys
import cmd
import time
from colorama import init, Fore, Back, Style

# Initialize colorama output
init()

def print_banner():
    banner = f"""
{Fore.CYAN}██████╗ ██╗  ██╗     ██████╗ ██████╗ ███████╗██████╗  █████╗ ████████╗ ██████╗ ██████╗ 
██╔══██╗╚██╗██╔╝    ██╔═══██╗██╔══██╗██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔═══██╗██╔══██╗
██████╔╝ ╚███╔╝     ██║   ██║██████╔╝█████╗  ██████╔╝███████║   ██║   ██║   ██║██████╔╝
██╔══██╗ ██╔██╗     ██║   ██║██╔═══╝ ██╔══╝  ██╔══██╗██╔══██║   ██║   ██║   ██║██╔══██╗
██████╔╝██╔╝ ██╗    ╚██████╔╝██║     ███████╗██║  ██║██║  ██║   ██║   ╚██████╔╝██║  ██║
╚═════╝ ╚═╝  ╚═╝     ╚═════╝ ╚═╝     ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝ ╚═╝  ╚═╝{Style.RESET_ALL}
{Fore.GREEN}[ Advanced Matrix Operations Suite v1.0 ]{Style.RESET_ALL}
"""
    return banner

class SparseMatrixCmd(cmd.Cmd):
    intro = print_banner() + '\nWelcome to the BX Operator CLI. Type help or ? to list commands.\n'
    prompt = f'{Fore.CYAN}BX>{Style.RESET_ALL} '

    def print_help_menu(self):
        """Print a detailed help menu with documentation"""
        help_text = f"""
{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗
║                     BX OPERATOR - HELP MENU                      ║
╚══════════════════════════════════════════════════════════════════╝{Style.RESET_ALL}

{Fore.GREEN}AVAILABLE COMMANDS:{Style.RESET_ALL}
━━━━━━━━━━━━━━━━━━

{Fore.YELLOW}1. LOADING AND DISPLAYING MATRICES{Style.RESET_ALL}
   • {Fore.CYAN}load{Style.RESET_ALL} <file_path1> <file_path2>
     └─ Load two matrices from specified files
     └─ Example: load matrix1.txt matrix2.txt

   • {Fore.CYAN}show{Style.RESET_ALL}
     └─ Display both loaded matrices
     └─ Shows formatted output with clear separation

   • {Fore.CYAN}opp{Style.RESET_ALL} <operation>
     └─ Checks if the operation is possible first
     └─ Perform matrix operation
     └─ Supported ops: +, -, *
     └─ Example: opp *

{Fore.YELLOW}3. ADVANCED FUNCTIONS{Style.RESET_ALL}
   • {Fore.CYAN}csr{Style.RESET_ALL}
     └─ Checks if the operation is possible first
     └─ Perfoms matrix operation with the csr approach
     └─ supported operations: +, -, *
     └─ Example: csr +

   • {Fore.CYAN}t{Style.RESET_ALL}
     └─ Transpose first matrix
     └─ Displays the transposed result

{Fore.YELLOW}4. SYSTEM COMMANDS{Style.RESET_ALL}
   • {Fore.CYAN}help{Style.RESET_ALL}
     └─ Display this help menu
   
   • {Fore.CYAN}exit{Style.RESET_ALL}
     └─ Exit the application

{Fore.GREEN}FILE FORMAT REQUIREMENTS:{Style.RESET_ALL}
━━━━━━━━━━━━━━━━━━━━━━━
• Input files should contain space-separated numbers
• Each line represents a row in the matrix
• All rows must have the same number of columns
• Example format:
  (1, 0, 0)
  (0, 1, 0)
  (0, 0, 1)

{Fore.GREEN}USAGE TIPS:{Style.RESET_ALL}
━━━━━━━━━━━
• Always load matrices before performing operations
• Use check command before operations to verify compatibility
• CSR format is useful for sparse matrix optimization
• Matrix dimensions must be compatible for operations:
  ├─ Addition/Subtraction: Matrices must have same dimensions
  └─ Multiplication: Columns of first matrix must equal rows of second

{Fore.GREEN}ERROR HANDLING:{Style.RESET_ALL}
━━━━━━━━━━━━━━━
• ✓ Success indicators show when operations complete
• ✗ Error messages explain why operations fail
• Loading errors indicate file format issues
• Dimension mismatch errors show specific requirements
"""
        print(help_text)

    def do_help(self, arg):
        'Show detailed help menu: help'
        self.print_help_menu()

    def __init__(self):
        super().__init__()
        self.matrix1 = None
        self.matrix2 = None

    def loading_animation(self, duration=0.2):
        """Display a loading animation"""
        chars = "⠋⠙⠹⠸⠼⠴⠦⠧⠇⠏"
        for _ in range(10):
            for char in chars:
                sys.stdout.write(f'\r{Fore.YELLOW}Processing {char}{Style.RESET_ALL}')
                sys.stdout.flush()
                time.sleep(duration/200)
        sys.stdout.write('\r' + ' ' * 20 + '\r')

    def print_matrix(self, matrix, title, timer=0):
        """Pretty print a matrix with formatting"""
        print(f'\n{Fore.GREEN}{title}{Style.RESET_ALL}')
        print(f'{Fore.YELLOW}{"=" * (len(title) + 2)}{Style.RESET_ALL}')
        for row in matrix.data:
            formatted_row = ' '.join(f'{Fore.CYAN}{val:4}{Style.RESET_ALL}' for val in row)
            print(formatted_row)
        print()
        print(f'\n{Fore.GREEN} Time Took: {Style.RESET_ALL}{timer}{Style.RESET_ALL}')

    def do_load(self, arg):
        'Load matrices from two files: load <file_path1> <file_path2>'
        try:
            file_path1, file_path2 = arg.split()
            self.loading_animation()
            parsed1, rows1, columns1, parsed2, rows2, columns2 = file_parser(file_path1, file_path2)
            self.matrix1 = SparseMatrix(parsed1, rows1, columns1)
            self.matrix2 = SparseMatrix(parsed2, rows2, columns2)
            print(f'{Fore.GREEN}✓ Matrices loaded successfully.{Style.RESET_ALL}')
        except Exception as e:
            print(f'{Fore.RED}✗ Error loading matrices: {e}{Style.RESET_ALL}')

    def do_show(self, arg):
        'Show the loaded matrices: show'
        try:
            if self.matrix1 and self.matrix2:
                self.print_matrix(self.matrix1, "Matrix 1")
                self.print_matrix(self.matrix2, "Matrix 2")
            else:
                print(f'{Fore.RED}✗ Matrices not loaded. Use the load command first.{Style.RESET_ALL}')
        except AttributeError:
            print(f'{Fore.RED}✗ Matrices not loaded. Use the load command first.{Style.RESET_ALL}')

    def check(self, arg):
        'Check if an operation can be performed on the matrices: check <operation>'
        try:
            if self.matrix1 and self.matrix2:
                operation = arg.strip()
                self.loading_animation(0.5)
                if operaction_checker(self.matrix1, self.matrix2, operation):
                    print(f'{Fore.GREEN}✓ The operation {operation} can be performed on the matrices.{Style.RESET_ALL}')
                    return True
                else:
                    if operation in ['+', '-']:
                        print(f"{Fore.RED}✗ Unequal Dimensions: row1 != row2 or col1 != col2{Style.RESET_ALL}")
                    elif operation == '*':
                        print(f"{Fore.RED}✗ Incompatible Dimensions: row1 != col2 or col1 != row2{Style.RESET_ALL}")
                    return False
            else:
                print(f'{Fore.RED}✗ Matrices not loaded. Use the load command first.{Style.RESET_ALL}')
                return False
        except AttributeError:
            print(f'{Fore.RED}✗ Matrices not loaded. Use the load command first.{Style.RESET_ALL}')
            return False

    def do_opp(self, arg):
        'Perform operations on the matrices: opp <operation>'
        operation = arg.strip()
        if self.check(operation):
            self.loading_animation()
            ops = Operations(self.matrix1, self.matrix2, operation)
            if operation == '+':
                start_time = time.time()
                result = ops.addition()
                self.print_matrix(result, "Matrix 1 + Matrix 2", time.time() - start_time )
            elif operation == '-':
                start_time = time.time()
                result = ops.subtraction()
                self.print_matrix(result, "Matrix 1 - Matrix 2", time.time() - start_time )
            elif operation == '*':
                start_time = time.time()
                result = ops.multiplication()
                self.print_matrix(result, "Matrix 1 * Matrix 2", time.time() - start_time )


    def do_t(self, arg):
        'Transpose the first loaded matrix: t'
        try:
            if self.matrix1 and self.matrix2:
                self.loading_animation()
                transposed_matrix = self.matrix1.transpose()
                self.print_matrix(transposed_matrix, "Transposed Matrix 1")
                transposed_matrix = self.matrix2.transpose()
                self.print_matrix(transposed_matrix, "Transposed Matrix 2")
            else:
                print(f'{Fore.RED}✗ Matrix not loaded. Use the load command first.{Style.RESET_ALL}')
        except AttributeError:
            print(f'{Fore.RED}✗ Matrix not loaded. Use the load command first.{Style.RESET_ALL}')

    def do_exit(self, arg):
        'Exit the CLI: exit'
        print(f'\n{Fore.YELLOW}Thank you for using BX OPERATOR!{Style.RESET_ALL}')
        self.loading_animation(0.5)
        print(f'{Fore.GREEN}Goodbye!{Style.RESET_ALL}')
        return True

if __name__ == '__main__':
    SparseMatrixCmd().cmdloop()