#!/usr/bin/python3


def safe_print_integer(value):
    """
         to safe print intger
    """
    try:
        print("{:d}".format(int(value)))
    except ValueError:
        return (False)
    return (True)
