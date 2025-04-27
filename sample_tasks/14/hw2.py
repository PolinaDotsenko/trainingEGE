#1
# for x in range(0, 10):
#     a = int(f"{str(x)}b09", 17)
#     b = int(f"{str(x)}8e8", 15)
#     if (a + b) % 155 == 0:
#         print((a + b) // 155)


#2?????
"""неправильно. операнды выражения уже записаны в указанных сс. 
надо переводить в десятичную. как в №1"""
# def convert(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     lst = [str(x) for x in lst][::-1]
#     return int("".join(lst))

# for x in range(11):
#     for y in range(11):
#         a = convert(int(f"{str(x)}341{str(y)}"), 11)
#         b = y + 1 * 19 + x * 19**2 + 6 * 19**3 + 5 * 19**4
#         if (a + b) % 305 == 0:
#             print((a + b) / 305)


#3
# for x in range(16):
#     n = int(f"8{str(x)}84{str(x)}", 16) + int(f"78{str(x)}34", 16)
#     if n % 23 == 0:
#         print(n // 23)


#4
# def convert(n , base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     return lst[::-1]

# n = 49**6 * 7**19 - 7**9 - 21
# print(convert(n, 7).count(6))


#5
# def convert(n, base):
#     lst = []
#     while n > 0:
#         lst.append(n % base)
#         n = n // base
#     lst = [str(x) for x in lst][::-1]
#     return int("".join(lst))

# for x in range(8):
#     for y in range(8):
#         a = convert(int(f"{str(y)}04{str(x)}5"), 11)
#         b = int(oct(int(f"253{str(x)}{str(y)}"))[2:])
#         if (a + b) % 117 == 0:
#             print((a + b) // 117)

# for x in range(8):!!!!!!
#     for y in range(8):
#         a = int(f"{str(y)}04{str(x)}5", 11)
#         b = int(f"253{str(x)}{str(y)}", 8)
#         if (a + b) % 117 == 0:
#             print((a + b) // 117)


#6
# for x in range(10):
#     a = int(f"3{str(x)}da", 14)
#     b = int(f"5{str(x)}a6", 12)
#     if (a + b) % 81 == 0:
#         print((a + b) // 81)


#7
# for x in range(16):
#     if x == 10:
#         x = "a"
#     if x == 11:
#         x = "b"
#     if x == 12:
#         x = "c"
#     if x == 13:
#         x = "d"
#     if x == 14:
#         x = "e"
#     if x == 15:
#         x = "f"
#     n = int(f"1{str(x)}bad", 16) + int(f"2c{str(x)}fe", 16)
#     if n % 15 == 0:
#         print(n // 15)
