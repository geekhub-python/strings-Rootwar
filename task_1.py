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
string_even = ''

for i, s in enumerate(string):
    if i % 2 == 0:
        continue
    string_even += s

print('6.All symbols with even index at string: ', string_even)

#7
string_odd = ''

for i, s in enumerate(string):
    if i % 2 != 0:
        continue
    string_odd += s

print('7.All symbols with odd index at string: ', string_odd)

#8
string_reverse = []

for s in string:
    string_reverse.append(s)

string_reverse.reverse()

print('8.Reverse symbols at string: ', ''.join(string_reverse))

#9
string_reverse = []
string_even = ''

for s in string:
    string_reverse.append(s)
string_reverse.reverse()

for i, s in enumerate(string):
    if i % 2 == 0:
        s = string_reverse[i]
    string_even += s

print('9.Reverse odd symbols at string: ', string_even)
