'''
Created Sep 24, 2024
Last Updated Sep 24, 2024

@author: Jerry Lu
@version: 0.1.0

0.1.0 Summary:
assumptions:
    -all relevant code of the codebase is in one root folder (neglects library functions for now)
    -there is a main execution file with a main function
    -
code flow:
    1. reads through codebase and parse through every .py file to gather all function definitions of the codebase
        -stores this in a dictionary?
            {"file1": [{"func1": ["sub_func1, sub_func2, ...],
                        "func2": ["sub_func1, sub_func2, ...],
                        ...
                        }],
             "file2": [{"func1": ["sub_func1, sub_func2, ...],
                        "func2": ["sub_func1, sub_func2, ...],
                        ...
                        }],
             ...
            }
    2. finds the main execution file and its main function
    3. create a second data structure that restructures and embeds the first structure into the second:
        -starting at main, ou
    4. outputs a sequential, hierarchical list of function calls that the
        program execution runs through.

TODO:


'''

import os
import re

def read_py(py_path):
    with open(py_path, 'r') as file:
        return file.read()

# Extract function names from a file 
def parse_py_function_names(py_file):
    function_names = []
    for line in py_file.split('\n'):
        if 'def ' in line:
            function_name = re.search(r'def\s+(\w+)', line).group(1)
            function_names.append(function_name)
    return function_names

# Extract function calls inside a function
def parse_py_function_calls(py_func):
    function_calls = []
    for line in py_func:
        if 


if __name__ == "__main__":
    py_path = "./TestPythonCodeBase/atmel_TestBed.py"
    code = read_py(py_path)
    print(type(code))
