#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
     prints possible numer of elements
    """
    try:
        count = 0
        for i in range(x):
            count += 1
            print("{}".format(my_list[i]), end="")
        else:
            print()
            return (count)
    except IndexError:
        print("")
        return (count - 1)
