
#* дан адрес узла и маска
#* просят найти ip-адресы узлов в этой сети,
#*  удовлетворяющие условию

from ipaddress import *

net = ip_network('адрес сети/адрес маска')
for i in net:
    ip1 = f'{i:b}'
    ip2 = bin(int(i))[2:].zfill(32)
    if # условие 


#* дан адрес узла и адрес сети
#* просят найти маску

from ipaddress import *

for mask in range(33):
    net = ip_network(f'адрес узла/{mask}', 0)
    print(net, net.netmask)

    # далее ищем ответ на вопрос в терминале