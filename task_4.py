#!/usr/bin/env python3

string = input('Enter your string: ')
escape = string.find(' ');

new_string = string[escape+1:] + ' ' + string[:escape]

print(new_string)