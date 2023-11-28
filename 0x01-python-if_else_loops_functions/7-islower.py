#!/usr/bin/python3
def islower(c):
    islower = __import__('7-islower').islower
    print("{:d} is {}".format(c, "lower" if islower("a") else "upper"))
