#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

y = abs(number) % 10

if number < 0:
    y = y * -1
    print(f"Last digit of {number} is {y} and is less than 6 and not 0")
    exit
else:
    if y == 0:
        print(f"Last digit of {number} is {y} and is 0")

    if y != 0 and y < 6:
        print(f"Last digit of {number} is {y} and is less than 6 and not 0")

    if y > 5:
        print(f"Last digit of {number} is {y} and is greater than 5")
