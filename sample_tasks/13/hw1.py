#1      base
# from ipaddress import *

# for mask in range(33):
#     net = ip_network(f"98.162.198.94/{mask}", 0)
#     print(net)


#2
from ipaddress import *

maxi = 0
for mask in range(33):
    net = ip_network(f"98.162.71.94/{mask}", 0)
    if str(net) == f'98.162.71.64/{mask}':
        maxi = max(maxi, net.num_addresses)
print(maxi)


#3
# from ipaddress import *

# net = ip_network("237.195.158.37/255.255.192.0", 0)
# print(net)


#4
# from ipaddress import *

# net = ip_network("249.17.100.96/255.255.224.0", 0)
# print(net)


#5
# from ipaddress import *

# for mask in range(33):
#     net1 = ip_network(f"98.162.71.151/{mask}", 0)
#     print(net1)


#6 



#7
# from ipaddress import *
# ip1 = '120.91.176.213'
# ip2 = '120.91.174.205'
# for mask in range(32 + 1):
#   net1 = ip_network(f'{ip1}/{mask}', 0)
#   net2 = ip_network(f'{ip2}/{mask}', 0)
#   # Проверяем, равны ли адреса сетей
#   if net2.network_address == net1.network_address and ip1 != net1.network_address and \
#       ip2 != net2.network_address and ip1 != net1.broadcast_address and ip2 != net2.broadcast_address:
#     print(net2.netmask)
#   # Ответом будет минимальное число в выводе