#!/usr/bin/python3
number = random.randint(-10 , 10)
if number < 0:
    print(f"{number} is negative")
elif number > 0:
    print(f"{number} is positive")
else:
    print(f"{number} is zero")
