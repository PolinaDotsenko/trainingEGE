#1 
# def convert(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     return lst[::-1]

# n = 6 * 343**1156 - 5 * 49**1147 + 4 * 7**1153 - 875
# print(sum(convert(n, 7)))


#2
# def convert(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     return lst[::-1]

# n = 6**333 - 5 * 6**215 + 3 * 6**144 - 85
# print(convert(n, 6).count(5))


#3
# def convert(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     return lst[::-1]

# n = 3 * 11**58 + 15 * 11**55 - 99 * 11**18 + 125 * 11**9 + 381
# print(len(set(convert(n, 11))))


#4
# n = 16**44 * 16**30 - (32**5 * (8**40 - 8**32) * (16**17 - 32**4))
# hx = hex(n)[2::]
# hx = hx.replace("e", "1")
# print(hx.count("1"))


#5
# def convert(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     return lst[::-1]

# for x in range(1, 1000):
#     n = 36**17 - 6**x + 71
#     if sum(convert(n, 6)) == 61:
#         print(x)


#6  (other type)
# for x in range(2, 36):
#     if int("101", x) + 13 == int("101", x + 1):
#         print(x)


#7
# for x in range(0, 109):
#     n = (1 + 5 * 109 + 7 * 109**2 + x * 109**3) + (x + 7 * 215 + 3 * 215**2 + 2 * 215**3)
#     if n % 567 == 0:
#         print(n / 567)


#8
# for x in range(98):
#     n = (5 + 4 * 98 + x * 98**2 + 2 * 98**3 + 98**4) + (8 + 9 * 123 + x * 123**2 + 123**3)
#     if n % 123 == 0:
#         print(n / 123)


#9
# n = int("36053", 8) - int("4773", 8)
# print(n)