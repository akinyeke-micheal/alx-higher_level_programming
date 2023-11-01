#!/usr/bin/python3
for numbers in range(100):
    formatted_number = str(numbers).zfill(2)
    print(formatted_number, end=', ' if numbers < 99 else '\n')
