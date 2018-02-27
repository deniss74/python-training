#!/usr/bin/python3

from sys import argv

file = argv[1]

ignore = ['duplex', 'alias', 'Current configuration']

with open(file, 'r') as f:
    for line in f:
        if line.startswith('!') != True:
            print(line.rstrip())

