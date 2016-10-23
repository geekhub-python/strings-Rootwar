#!/usr/bin/env python3

string = input('Enter your string: ')

if string.find('f') == string.rfind('f') >= 0:
    print("Index 'f' at string : ", string.find('f'))
elif string.find('f') != string.rfind('f'):
    print("First index 'f' at string: ", string.find('f'))
    print("Last index 'f' at string: ", string.rfind('f'))