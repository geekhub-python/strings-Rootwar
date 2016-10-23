#!/usr/bin/env python3

string = input('Enter your string: ')
substring = string[string.find('h'):string.rfind('h')+1]
new_string = string.replace(substring, '')

print('New string: ', new_string)