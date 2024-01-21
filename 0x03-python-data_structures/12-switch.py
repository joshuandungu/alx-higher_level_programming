#!/usr/bin/python3
a = 89
b = 10

def switch_numbers(a, b):
    a , b  = b, a
    return a,b
a, b = switch_numbers(a, b)
print("a={:d} - b={:d}".format(a, b))
