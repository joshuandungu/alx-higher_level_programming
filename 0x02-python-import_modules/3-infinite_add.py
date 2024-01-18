#!/usr/bin/python3
import sys

if __name__ == '__main__':
    arg = sys.argv
    k = len(arg)
    sum = 0

    if k > 1:
        for x in range(1, k):
            sum += int(arg[x])

    print(sum)
