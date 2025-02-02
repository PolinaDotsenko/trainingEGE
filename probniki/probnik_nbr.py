

#13
# from ipaddress import *

# n = []
# c = 0
# net = ip_network("202.75.38.160/255.255.255.240")
# for ip in net:
#     n.append(bin(int(ip)))
#     for i in n:
#         if "111" in i:
#             c += 1
    
# print(c)


#14
# numb = (4 * (8**3032)) + (3 * (16**1956)) + 870
# def convert(n, base):
#     s = ""
#     while n > 0:
#         s = str(n % base) + s
#         n = n // base
#     return s
    
# sevnum = str(convert(numb, 7))
# print((3 * sevnum.count("3")) - sevnum.count("1"))


#12
# ans = []
# for n in range(4, 10000):
#     s = "1" + n * "2"
#     while "12" in s or "322" in s or "222" in s:
#         if "12" in s:
#             s = s.replace("12", "2", 1)
#         if "322" in s:
#             s = s.replace("322", "21", 1)
#         if "222" in s:
#             s = s.replace("222", "3", 1)
#     summa = sum([int(i) for i in s])
#     ans.append(summa)
# print(max(ans))