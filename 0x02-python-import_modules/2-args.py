#!/usr/bin/python3
import sys

if __name__ == '__main__':
    """Prints the argument list passed to the program

    The program takes all the arguments starting from the second
    and prints the number of arguments and their value

    """
    av = sys.argv
    args = len(av) - 1

    if args > 1:
        print(args, 'arguments:')
        for i in range(1, args + 1):
            print('{:d}: {}'.format(m, av[m]))
    elif args == 1:
        print(args, 'argument:')
        for m in range(1, args + 1):
            print('{:d}: {}'.format(m, av[m]))
    elif args == 0:
        print(args, 'arguments.')
