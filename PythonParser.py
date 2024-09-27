'''
Created Sep 24, 2024
Last Updated Sep 24, 2024

@author: Jerry Lu
@version: 0.1.0

0.1.0 Summary:
assumptions:
    -all relevant code of the codebase is in one root folder (neglects library functions for now)
    -there is a main execution file with a main function
    -all code is executed within some function. The codebase has no lone code in a script or scripts.
code flow:
    1. reads through codebase and parse through every .py file to gather all function definitions
        of the codebase by taking advantage of the keyword "def" in every function header.
        -stores this in a dictionary?
            ex1:
            {"file1": ["func1", "func2", ...],
             "file2": ["func1", "func2", ...],
             ...
            }
    2. finds the main execution file and its main function
    3. Parse through the main function, looking for likely function calls using regex and checking likely
        functions against the known list of functions in the dictionary above. Function calls are recorded
        in a second data structure, and the parser repeats by going into each of those function calls and
        recording the function calls in them until all function calls have been parsed through.
        -stores this in a dictionary:
            {"main": {"func_call1": {"sub_func_call1:{}},
                        "func_call2": {}
                    }
            }
    4. outputs a sequential, hierarchical list of function calls that the program execution runs through,,
        starting at the specified function.



TODO:


'''

import os
import re

# Extract function names from function headers in a file 
def parse_py_function_names(py_file):
    function_names = []
    for line in py_file.split('\n'):
        if 'def ' in line:
            function_name = re.search(r'def\s+(\w+)', line).group(1)
            function_names.append(function_name)
    return function_names

def read_py(py_file_path):
    with open(py_file_path, 'r') as file:
        return file.read()

# Parse through entire codebase to create a list of all functions in the codebase
# {"file1": ["func1", "func2", ...],
#              "file2": ["func1", "func2", ...],
#              ...
#             }
def parse_py_codebase_functions(py_codebase_path):
    pass


# Extract function calls inside a function
def parse_py_function_calls(py_func):
    function_calls = []
    # need to identify the start and end of a function
    # need to identify a possible function call

def parse_py_codebase_execution(py_start_file, py_start_function, codebase_functions):
    pass

s
def main():
    py_codebase_path = ""
    py_start_file = ""
    py_start_function = ""
    codebase_functions = parse_py_codebase_functions(py_codebase_path)
    parse_py_codebase_execution(py_start_file, py_start_function, codebase_functions)

if __name__ == "__main__":
    main()
