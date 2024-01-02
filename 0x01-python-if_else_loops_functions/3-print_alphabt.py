#!/usr/bin/python3
for num in range(ord('a'), ord('z') + 1):
    if num != ord('q') and num != ord('e'):
        print("{:c}".format(num), end="")
