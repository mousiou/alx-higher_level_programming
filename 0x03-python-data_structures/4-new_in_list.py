#!/usr/bin/python3

def new_in_list(my_list, idx, element):
    list_c = my_list.copy()
    if idx < 0:
        return list_c
    elif idx > len(my_list) - 1:
        return list_c
    else:
        list_c[idx] = element
        return list_c
