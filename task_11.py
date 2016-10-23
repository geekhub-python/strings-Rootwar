#!/usr/bin/env python3

string = input('Enter your string: ')
substring = string[string.find('h') + 1:string.rfind('h')]
substring_reverse = []

for s in substring:
    substring_reverse.append(s)
substring_reverse.reverse()

print('New string: ', string.replace(substring, ''.join(substring_reverse)))