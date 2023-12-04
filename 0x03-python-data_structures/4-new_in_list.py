#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if (idx < 0) or (idx >= len(my_list)):
        return my_list

    my_New_list = my_list.copy()
    my_New_list[idx] = element
    return my_New_list
