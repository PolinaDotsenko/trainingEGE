#1
# for i in range(1, 100):
#     n = bin(i)[2:]
#     n = n + str(n.count("1") % 2)
#     n = n + str(n.count("1") % 2)
#     r = int(n, 2)
#     if r > 77:
#         print(i)


#2
# for i in range(1, 100):
#     n = bin(i)[2:]
#     n = n + str(n.count("1") % 2)
#     n = n + str(n.count("1") % 2)
#     r = int(n, 2)
#     if r > 97:
#         print(i)
#         break


#3
# for i in range(1, 200):
#     n = bin(i)[2:]
#     if i % 2 == 0:
#         n += "00"
#     else:
#         n += "11"
#     r = int(n, 2)
#     if r > 115:
#         print(i)
#         break


#5 
# def f(n, base):
#     s = ""
#     while n > 0:
#         s = str(n % base) + s
#         n = n // base
#     return s

# lst = []
# for i in range(1, 100):
#     n = f(i, 6)
#     if i % 3 == 0:
#         n += n[:2]
#     else:
#         n += f(i % 3 * 10, 6)
#         r = int(n, 6)
#         if r > 680:
#             lst.append(r)
# print(min(lst))


#6
# for N in range(1, 1000):
#     n = bin(N)[2:]
#     if n.count("1") > n.count("0"):
#         n += "0"
#     else:
#         n += "11"
#     r = int(n, 2)
#     if r > 2019:
#         print(N)
#         break