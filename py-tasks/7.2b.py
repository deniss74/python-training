#!/usr/bin/python3

from sys import argv

file = argv[1]

ignore = ['duplex', 'alias', 'Current configuration']

with open(file, 'r') as src, open('config_sw1_cleared.txt', 'w') as dest:
    for line in src:
        for start in ignore:
            if line.lstrip().startswith(start):
                break
        else:
            dest.write(line)

