#!/usr/bin/python3
def islower(c: str) -> bool:
    if ord(c) >= ord('a') and ord(c) <= ord('z'):
        return True
    else:
        return False
