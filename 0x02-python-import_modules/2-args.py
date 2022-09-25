#!/usr/bin/python3
from sys import argv

if __name__ == '__main__':
    lon = len(argv) - 1
    i = 1
    if lon == 1:
        print(lon, 'argument:')
    elif lon == 0:
        print(lon, 'arguments.')
    else:
        print(lon, 'arguments:')
    for av in argv:
        if i <= lon:
            print("{:d}: {}".format(i, argv[i]))
            i = i + 1
