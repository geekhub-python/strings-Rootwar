#!/usr/bin/env python3

string = input('Enter your string: ')
string = string.strip(' ')

quantity = string.count(' ')

print('String has %s word' % (quantity + 1))

