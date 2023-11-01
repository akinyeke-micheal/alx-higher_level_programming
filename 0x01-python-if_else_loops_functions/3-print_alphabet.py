#!/usr/bin/python3
for alphabet in range(97, 123):
    letter = chr(alphabet)
    if letter not in ('q', 'e'):
        print("{}".format(letter), end="")
