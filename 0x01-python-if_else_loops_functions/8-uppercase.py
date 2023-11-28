#!/usr/bin/python3
def uppercase(s):
    for x in s:
        ascii_value = ord(x)
        if 97 <= ascii_value <= 122:
            ascii_value -= 32  # Convert lowercase to uppercase
        print("{}".format(chr(ascii_value)), end="")
    print()  # Add a new line at the end
