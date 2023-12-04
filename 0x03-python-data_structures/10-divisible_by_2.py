#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    divlist = []
    for i in my_list:
        if my_list[i] % 2 == 0:
            divlist.append(True)
        else:
            divlist.append(False)
    return divlist
