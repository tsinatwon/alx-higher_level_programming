#!/usr/bin/python3


def safe_print_integer(value):
    """
         to safe print intger
    """
    try:
        value2 = int(value)
        print("{:d}".format(value))
        return (True)
    except ValueError:
        return (False)
