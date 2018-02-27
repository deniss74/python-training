#!/usr/bin/python3

templ1 = '{0:23} {1:} {2:23} {3:} {4:23} {5:} {6:23} {7:} {8:23} {9:} {10:23} {11:}'

with open('ospf.txt', 'r') as f:
    for line in f:
        if line.startswith('O'):
            route = line.split()
            print(templ1.format('\nProtocol:', 'OSPF', '\nPrefix:', route[1], '\nAD/Metric:', route[2], '\nNext-Hop:', route[4].rstrip(','), '\nLast update:', route[5].rstrip(','), '\nOutbound Interface:', route[6]))

