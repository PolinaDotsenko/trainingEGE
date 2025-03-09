#1
# from ipaddress import *

# c = 0
# net = ip_network("202.75.38.152/255.255.255.248")
# for ip in net:
#     n = f"{ip:b}" #способ для более новой версии питона
#     #n = bin(int(ip))[2:].zfill(32)
#     if "111" in n:
#         c += 1
# print(c)


#2
# from ipaddress import *

# for mask in range(33):
#     net = ip_network(f"111.81.208.27/{mask}", 0)
#     print(net, net.netmask)


#3
# from ipaddress import *

# for mask in range(33):
#     net = ip_network(f"215.181.200.27/{mask}", 0)
#     print(net, net.netmask)


#4
# from ipaddress import *

# c = 0
# net = ip_network("158.132.161.128/255.255.255.128")
# for ip in net:
#     n = f"{ip:b}"
#     if n[-1] == "1":
#         c += 1
# print(c)


#5
# from ipaddress import *

# c = 0
# net = ip_network("115.198.0.0/255.254.0.0")
# for ip in net:
#     n = f"{ip:b}"
#     if n.count("1") % 5 == 0:
#         c += 1
# print(c)


#6
# from ipaddress import *

# c = 0
# net = ip_network("112.160.0.0/255.240.0.0")
# for ip in net:
#     n = f"{ip:b}"
#     if n.count("1") % 3 != 0:
#         c += 1
# print(c)


#7
# from ipaddress import *

# c = 0
# net = ip_network("192.168.32.160/255.255.255.240")
# for ip in net:
#     n = f"{ip:b}"
#     if n.count("0") > 21:
#         c += 1
# print(c)


#8*
# from ipaddress import *

# for mask in range(32, -1, -1):
#     net = ip_network(f"154.63.206.129/{mask}", 0)
#     if ip_address("154.63.100.75") in net:
#         c = 0
#         for ip in net:
#             n = f"{ip:b}"
#             if n.count("1") % 2 == 0:
#                 c += 1
#         print(c)
#         break


#9
# from ipaddress import *

# c = 0
# net = ip_network("106.184.0.0/255.248.0.0")
# for ip in net:
#     n = f"{ip:b}"
#     if n.count("1") % 2 != 0:
#         c += 1
# print(c)