#!/usr/bin/python3

netw_templ = '\nNetwork:\n{0:<8} {1:<8} {2:<8} {3:<8}\n{0:<08b} {1:<08b} {2:<08b} {3:<08b}\n'
mask_templ = "\nMask:\n/{}"


a = input('Enter netw/mask:\n')

net = a.split('/')[0].split('.')
for i in range(4):
    net[i] = int(net[i])

mask = int(a.split('/')[1])


print(netw_templ.format(net[0], net[1], net[2], net[3]))
print(mask_templ.format(mask))
