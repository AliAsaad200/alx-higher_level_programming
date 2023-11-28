#!/usr/bin/python3
for x in range(ord('a'), ord('z') + 1):
    if(x == "q" or "e"):
        continue;
        print("{:c}".format(x), end='')
