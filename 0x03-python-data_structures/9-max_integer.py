def max_integer(my_list=[]):
    if not my_list:
        return None
    num = min(my_list)
    for i in my_list:
        if i > num:
            num = i
    return num
