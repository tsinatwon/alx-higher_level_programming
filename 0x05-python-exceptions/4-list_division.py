#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    """
        divide list element index by inedx
    """
    lst = []
    counter = 0
    while counter < list_length:
        res = 0
        try:
            res = my_list_1[counter] / my_list_2[counter]
        except ZeroDivisionError:
            print("divistion by 0")
        except IndexError:
            print("out of range")
        except TypeError:
            print("wrong type")
        finally:
            lst.append(res)
        counter += 1
    return (lst)
