#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    my_dictionary = a_dictionary.copy()

    for k, v in my_dictionary.items():
        my_dictionary[k] = v * 2

    return my_dictionary
