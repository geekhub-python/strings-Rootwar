#!/usr/bin/env python3

string = input('Enter your string: ')
new_string = ''

for i, s in enumerate(string):
    if i % 3 == 0:
        continue
    new_string += s

print('New string: ', new_string)
