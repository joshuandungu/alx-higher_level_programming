#!/usr/bin/python3
from sys import argv
from calculator_1 import add, sub, mul, div

if __name__ == '__main__':
    """
    Handles basic operations

    Performs basic operations like addition, substraction,
    multiplication and division between two numbers.

    The program will execute an operation between two numbers
    selected by the operator sent to the program.
    """
    k = len(argv) - 1

    if k == 3:
        operator = argv[2]
        a = int(argv[1])
        b = int(argv[3])
        if operator == '+':
            res = add(a, b)
            print('{:d} + {:d} = {:d}'.format(a, b, res))
            exit(0)
        elif operator == '-':
            res = sub(a, b)
            print('{:d} - {:d} = {:d}'.format(a, b, res))
            exit(0)
        elif operator == '*':
            res = mul(a, b)
            print('{:d} * {:d} = {:d}'.format(a, b, res))
            exit(0)
        elif operator == '/':
            res = div(a, b)
            print('{:d} / {:d} = {:d}'.format(a, b, res))
            exit(0)
        else:
            print('Unknown operator. Available operators: +, -, * and /')
            exit(1)
    else:
        print('Usage: ./100-my_calculator.py <a> <operator> <b>')
        exit(1)
