#!/usr/bin/python3

def max_integer(my_list=[]):
    max_num = 0
    if len(my_list) > 0:
        for i in my_list:
            if i > max_num:
                max_num = my_list[i]
        return (max_num)
    else:
        return "None"
