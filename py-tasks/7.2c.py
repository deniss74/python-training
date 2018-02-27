#!/usr/bin/python3

from sys import argv

file1 = argv[1]
file2 = argv[2]

ignore = ['duplex', 'alias', 'Current configuration']

with open(file1, 'r') as src, open(file2, 'w') as dest:
    for line in src:
        for start in ignore:
            if line.lstrip().startswith(start):
                break
        else:
            dest.write(line)

