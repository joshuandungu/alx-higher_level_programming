#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    av = sys.argv
    m = len(av) - 1

    if m > 1:
        print(m, 'arguments:')
        for n in range(1, m + 1):
            print('{:d}: {}'.format(n, av[n]))
    elif m == 1:
        print(m, 'argument:')
        for i in range(1, m + 1):
            print('{:d}: {}'.format(n, av[n]))
    elif m == 0:
        print(m, 'arguments.')
