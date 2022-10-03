#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arg_vector = sys.argv
    len_argv = len(arg_vector) - 1
    if len_argv > 1:
        print(len_argv, 'arguments:')
        for i in range(1, len_argv + 1):
            print('{:d}: {}'.format(i, arg_vector[i]))
    elif len_argv == 1:
        print(len_argv, 'argument:')
        for i in range(1, len_argv + 1):
            print('{:d}: {}'.format(i, arg_vector[i]))
    elif len_argv == 0:
        print(len_argv, 'arguments.')
