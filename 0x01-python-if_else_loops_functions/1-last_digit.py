#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = number % 10 if number > 10 else number % -10
if (num2 > 5):
    print(f"Last digit of {number} is {num2} and is greater than 5")
elif (num2 == 0):
    print(f"Last digit of {number} is {num2} and is 0")
elif (number < 0):
    print(f"Last digit of {number} is {num2} and is less than 6 and not 0")
