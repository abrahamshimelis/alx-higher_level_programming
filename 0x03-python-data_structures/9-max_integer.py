def max_integer(my_list=[]):
    if not my_list:
        return None
    num = my_list[0]
    for i in my_list:
        if i > num:
            num = i
    return num
