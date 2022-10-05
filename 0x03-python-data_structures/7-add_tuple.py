#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    tuple_a = check_tuple(tuple_a)
    tuple_b = check_tuple(tuple_b)

    return ((tuple_a[0] + tuple_b[0]), (tuple_a[1] + tuple_b[1]))
def check_tuple(my_tuple=()):
    if len(my_tuple) < 2:
        if len(my_tuple) == 1:
            my_tuple = (my_tuple[0], 0)
        elif len(my_tuple) == 0:
            my_tuple = (0, 0)
    elif len(my_tuple) > 2:
        my_tuple = (my_tuple[0], my_tuple[1])
    return my_tuple
