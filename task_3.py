#!/usr/bin/env python3

import math

string = input('Enter your string: ')
length = len(string)
count_symbol = (length / 2)
count_symbol = math.ceil(count_symbol)

new_string = string[count_symbol:] + string[:count_symbol]

print(new_string)
