#!/usr/bin/python3
import sys
if __name__ == '__main__':
    arg_vector = sys.argv
    sum_total = 0
    len_argv = len(arg_vector) - 1
    if len_argv >= 0:
        if len_argv > 0:
            for i in range(1, len_argv + 1):
                if type(arg_vector[i-1]) == int:
                    sum_total = sum_total + arg_vector[i]
                else:
                    sum_total = sum_total + int((arg_vector[i]))
        print(sum_total)
