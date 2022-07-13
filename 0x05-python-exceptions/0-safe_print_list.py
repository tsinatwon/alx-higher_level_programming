#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
     prints possible numer of elements
    """
    try:
        for i in range(x):
            print("{}".format(my_list[i]), end="")
        else:
            print('\n')
            return (i + 1)
    except IndexError:
        print("")
        return (i)
