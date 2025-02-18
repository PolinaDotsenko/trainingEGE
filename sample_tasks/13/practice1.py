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