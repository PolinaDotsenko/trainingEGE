#1
# res = []
# for i in range(100, 3001):
#     n = bin(i)[2:]
#     lst = [x for x in n]
#     lst.remove(lst[0])
#     if lst[0] == "0":
#         n = "".join(lst)
#     if len(lst) == 0:
#         n = "0"
#     r = int(n, 2) 
#     res.append(i - r)
# print(len(set(res)))


#2
# for i in range(0, 100):
#     n = bin(i)[2:]
#     if i % 2 == 0:
#         n += "10"
#     else:
#         n += "01"
#     r = int(n, 2)
#     if r <= 102:
#         print(r)


#3
# for i in range(2, 1500):
#     n = bin(i)[2:]
#     chet1 = [x for x in n[1::2] if x == "1"]
#     nechet0 = [x for x in n[0::2] if x == "0"]
#     r = abs(len(chet1) - len(nechet0))
#     if r == 5:
#         print(i)
#         break


#4
# for i in range(0, 100):
#     n = bin(i)[2:]
#     if n.count("1") % 2 == 0:
#         n += "1"
#     else:
#         n += "0"
#     if n.count("1") % 2 == 0:
#         n += "1"
#     else:
#         n += "0"
#     r = int(n, 2)
#     if r > 54:
#         print(r)
#         break


#5
# for i in range(0, 100):
#     n = bin(i)[2:]
#     su = sum([int(x) for x in n])
#     n += str(su % 2)
#     n += str(su % 2)
#     r = int(n, 2)
#     if r > 43:
#         print(r)
#         break


#6
# for i in range(0, 101):
#     n = bin(i)[2:]
#     rev = [x for x in n[::-1]]
#     r = int("".join(rev), 2)
#     if r == 13:
#         print(i)


#7
# for i in range(2, 100):
#     n = bin(i)[2:]
#     n += n[-2]
#     n += n[1]
#     r = int(n, 2)
#     if r > 180:
#         print(i)
#         break


#8
# for i in range(0, 100):
#     n = bin(i)[2:]
#     su = sum([int(x) for x in n])
#     if su % 2 == 0:
#         n = "10" + n[2:] + "0"
#     else:
#         n = "11" + n[2:] + "1"
#     r = int(n, 2)
#     if r < 35:
#         print(i)