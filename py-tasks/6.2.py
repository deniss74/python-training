#!/usr/bin/python3

mac = ['aabb:cc80:7000', 'aabb:dd80:7340', 'aabb:ee80:7000', 'aabb:ff80:7000']

mac_cisco = []

for MAC in mac:
    MAC = MAC.replace(':', '.')
    mac_cisco.append(MAC)

print(mac_cisco)

