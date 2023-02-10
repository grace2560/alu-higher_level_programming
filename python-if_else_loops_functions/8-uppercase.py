#!/usr/bin/python3
def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= ord('a') and ord(str[i]) <= ord('z'):
            caps = ord(str[i]) + (ord('A') - ord('a'))
        else:
            caps = ord(str[i])
            print("{}". format(chr(caps)), end=("")
    print()
