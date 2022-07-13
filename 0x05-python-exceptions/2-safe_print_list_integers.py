#!/usr/bin/python3


def safe_print_list_integers(my_list=[], x=0):
    """
        to print safely inger
    """
    try:
        counter = 0
        holder = 0
        while counter < x:
            if isinstance(my_list[counter], int):
                print("{:d}".format(my_list[counter]), end="")
                counter += 1
                holder += 1
            else:
                counter += 1
        print()
    except (ValueError, TypeError):
        pass
    return holder
