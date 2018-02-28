#!/usr/bin/python3

with open('CAM_table.txt', 'r') as f:
    for line in f:
        if line.count('.') == 2:
            m1 = line.split()
            print('{0:7} {1:17} {2:}'.format(m1[0], m1[1], m1[3]))

