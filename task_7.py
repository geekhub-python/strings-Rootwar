#!/usr/bin/env python3

string = input('Enter your string: ')
substring = string[1:-1]

lower_h = string[0] + substring.replace('h', 'H') + string[-1]

print(lower_h)