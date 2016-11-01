#!/usr/bin/env python3

string = input('Enter your string: ')

#1
print('1.First symbol at string: ', string[0])

#2
print('2.Before last symbol at string: ', string[-2])

#3
print('3.First five symbols at string: ', string[0:5])

#4
print('4.All string and not two last symbol: ', string[:-2])

#5
print('5.String length: ', len(string))

#6
print('6.All symbols with even index at string: ', string[1::2])

#7
print('7.All symbols with odd index at string: ', string[::2])

#8
print('8.Reverse symbols at string: ', string[::-1])

#9
print('9.Reverse odd symbols at string: ', string[2:2:-1])
