#1 пример
# from ipaddress import *

# for mask in range(33):
#     net = ip_network(f"111.81.88.168/{mask}", 0)
#     print(net, net.netmask)


#2 пример
# from ipaddress import *

# for mask in range(33):
#     net = ip_network(f"133.191.169.34/{mask}", 0)
#     print(net)


#3 
# from ipaddress import *

# for mask in range(33):
#     net = ip_network(f"93.138.70.47/{mask}", 0)
#     print(net)


#4
# from ipaddress import *

# c = 0
# net = ip_network("172.16.168.0/255.255.248.0")
# for ip in net:
#     n = f"{ip:b}"
#     if n.count("1") % 5 != 0:
#         c += 1
# print(c)


#5
# mask = "255.255.254.0"
# s = mask.split(".")
# for i in s:
#     print(bin(int(i))[2:])
# #всего 8 нулей
# print("result:", 2**8 - 2)


#!!!6
# mask = "255.255.255.128"
# a = mask.split(".")
# for i in a:
#     print(bin(int(i))[2:])
# #всего 7 нулей
# print(2**7 - 2) 


#!!!7
# from ipaddress import *

# for mask in range(33):
#     net = ip_network(f"220.128.112.142/{mask}", 0)
#     a = str(net).split("/")
#     if a[0] == "220.128.96.0":
#         print(net.netmask)