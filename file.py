# def f(n):
#     if n <= 1: return 0
#     if n > 1 and n % 2 != 0: return f(n -1) + 3 * n * n
#     if n > 1 and n % 2 == 0: return n // 2 + f(n - 1) + 2

# print(f(49))


#12
# s = "*" * 200
# c = 0
# while "****" in s or "???" in s:
#     s = s.replace("****", "???", 1)
#     c += 3
#     s = s.replace("??", "*")
# print(c)


#12
# res = []
# for i in range(1, 1000):
#     s = "8" * i
#     while "555" in s or "888" in s:
#         s = s.replace("555", "8", 1)
#         s = s.replace("888", "55", 1)
#     if s not in res:
#         res.append(s)
# print(len(res))


#12
# res = []
# for i in range(1, 1000):
#     s = "5" * i
#     while "555" in s or "888" in s:
#         s = s.replace("555", "8", 1)
#         s = s.replace("888", "55", 1)
#     if s not in res:
#         res.append(s)
# print(len(res))


#5
# l = []
# for i in range(1, 13):
#     n = bin(i)[2:]
#     if i % 2 == 0: n = "10" + str(n)
#     if i % 2 != 0: n = "1" + str(n) + "01"
#     r = int(n, 2)
#     l.append(r)
# print(max(l))
    

#12
# s = "1" * 81
# while "11111" in  s or "888" in s:
#     if "11111" in  s: s = s.replace("11111", "88", 1)
#     else: s = s.replace("888", "8", 1)
# print(s)


#16
# from sys import *
# setrecursionlimit(10000)

# def f(n):
#     if n == 1: return 1
#     if n > 1: return (n - 1) * f(n - 1)
# print((f(2024) + 2 * f(2023)) / f(2022))


