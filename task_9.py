#!/usr/bin/env python3

string = input('Enter your string: ')
list_index = []

for i, s in enumerate(string):
    if s != 'f':
        continue
    list_index.append(i)

if len(list_index) >= 2:
    print(list_index[1])
elif len(list_index) == 1:
    print(-1)
else:
    print(-2)
