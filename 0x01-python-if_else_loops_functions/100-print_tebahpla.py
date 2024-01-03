#!/usr/bin/python3
for alph in range(25, -1, -1):
    ch = alph + ord('A')
    if alph % 2 == 0:
        ch = ch + 32
    print("{:c}".format(ch), end="")
