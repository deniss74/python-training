#!/usr/bin/python3

import sys

ip = input('Введите IP: ')

while len(ip) == 0:
    ip = input('Пустая строка, введите IP: ')

ipl = ip.split('.')

pass_correct = False

while not pass_correct:
    for octet in ipl:
        if octet.isdigit() and int(octet) in range(256):
            pass_correct = True
        else:
            pass_correct = False
            print('Incorrect IP address\n')
            ip = input('Введите IP: ')
            ipl = ip.split('.')
            break

octet1 = int(ip.split('.')[0])

if octet1 in range(1,224):
    print('unicast')
elif octet1 in range(224,240):
    print('multicast')
elif ip == "0.0.0.0":
    print('unassigned')
elif ip == '255.255.255.255':
    print('local broadcast')
else:
    print('unused')


