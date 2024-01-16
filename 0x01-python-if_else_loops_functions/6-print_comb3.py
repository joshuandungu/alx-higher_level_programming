#!/usr/bin/python3
for m in range(10):
    for n in range(10):
        if (m != n and m < n) and m < 9:
            if (m == 8 and n == 9):
                print('{0}{1}'.format(m, n))
            else:
                print('{0}{1}, '.format(m, n), end='')
               
