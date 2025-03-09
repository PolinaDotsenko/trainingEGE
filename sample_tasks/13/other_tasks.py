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