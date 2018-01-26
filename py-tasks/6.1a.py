#!/usr/bin/python3

import sys

ip = input('Введите IP: ')

while len(ip) == 0:
    ip = input('Пустая строка, введите IP: ')

ipl = ip.split('.')

for octet in ipl:
    if octet.isdigit() and int(octet) in range(256):
        pass
    else:
        print('Incorrect IP address')
        sys.exit()

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


