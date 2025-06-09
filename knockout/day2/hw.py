#1
# from ipaddress import *
#
# net = ip_network("129.130.131.128/255.255.192.0", 0)
# print(net)


#2
# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f"93.138.70.47/{mask}", 0)
#     print(net, net.netmask)


#3
# from ipaddress import *
#
# c = 0
# net = ip_network("124.8.0.0/255.248.0.0")
# for i in net:
#     ip = f"{i:b}"
#     c = max(c, ip.count("0"))
# print(c)


#4
# print(bin(224)[2:].zfill(8))
# print(2**5 - 2)


#5
# from ipaddress import *
#
# c = 0
# net = ip_network("99.64.0.0/255.192.0.0")
# for i in net:
#     ip = f"{i:b}"
#     if ip[-2:] == "11":
#         c += 1
# print(c)


#6
# from ipaddress import *
#
# net = ip_network("143.168.72.213/255.255.255.240", 0)
# for i in net:
#     print(i) #выбрать наибольший, !!!который может быть присвоен компьютеру!!!


#7
# from ipaddress import *
#
# net = ip_network("98.112.180.255/255.255.240.0", 0)
# for i in net:
#     print(i) #!!!который может быть присвоен компьютеру!!!


#8
# print([bin(x)[2:].zfill(8) for x in (121, 171, 15, 70)])
# print([bin(x)[2:].zfill(8) for x in (121, 171, 3, 68)])
# print(int("11110000", 2))


#9 два узла в разных сетях
# print([bin(x)[2:].zfill(8) for x in (154, 63, 206, 129)])
# print([bin(x)[2:].zfill(8) for x in (154, 63, 100, 75)])
# print(int("10000000", 2))


#10
# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f"93.138.88.47/{mask}", 0)
#     print(net)
# print(int("11110000", 2))


#11
# from ipaddress import *
#
# c = 0
# net = ip_network("122.159.136.144/255.255.255.248")
# for i in net:
#     ip = f"{i:b}"
#     if ip.count("1") % 4 != 0:
#         c += 1
# print(c)


#12
# print([bin(x)[2:].zfill(8) for x in (98, 162, 71, 151)])
# print([bin(x)[2:].zfill(8) for x in (98, 162, 71, 155)])
# 255 255 255 1111


#13
# from ipaddress import *
#
# for mask in range(33):
#     net = ip_network(f"98.162.71.94/{mask}", 0)
#     print(net, net.netmask)
# print(bin(192)[2:].zfill(8))
# print(bin(224)[2:].zfill(8))
# print(2**5)