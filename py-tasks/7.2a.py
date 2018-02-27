#!/usr/bin/python3

from sys import argv

file = argv[1]

ignore = ['duplex', 'alias', 'Current configuration', '!']

with open(file, 'r') as f:
    for line in f:
        for start in ignore:
            if line.lstrip().startswith(start):
                break
        else:
            print(line.rstrip())

