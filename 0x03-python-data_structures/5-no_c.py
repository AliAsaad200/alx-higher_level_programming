#!/usr/bin/python3
def no_c(my_string):
    my_new_string = ""
    for i in len(my_string):
        if i != "c" or i != "C":
            my_new_string += my_string[i]
    return my_new_string
