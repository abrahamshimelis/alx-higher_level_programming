#!/usr/python3
def uppercase(str):
    my_str = ""
    for i in range(len(str)):
        if (ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z')):
            my_str += chr(ord(str[i]) - 32)
            continue
        my_str += str[i]

    print('{0}'.format(my_str))
