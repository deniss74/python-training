#!/usr/bin/python3

ip = input('Введите IP: ')
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


