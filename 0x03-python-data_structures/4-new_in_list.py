#!/usr/bin/python3
def new_in_list(my_list, index, element):
    n = len(my_list)
    list_cpy = my_list.copy()
    if index < 0:
        return list_cpy
    elif index > n - 1:
        return list_cpy
    else:
        list_cpy[index] = element
        return 
