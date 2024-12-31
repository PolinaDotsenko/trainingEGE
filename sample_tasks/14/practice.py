#1
# n = (77 + 7 ** 77) * 7 ** 77 + 77 + 7 ** 7
# ###
# base = 7
# lst = []
# while n > 0:
#     lst.append(n % base)
#     n = n // base
# ###
# print(lst.count(1))


#2
# n = 5 ** 2004 - 5 ** 1016 - 25 ** 508 - 5 ** 400 + 25 ** 250 - 27
# base = 5
# lst = []
# while n > 0:
#     lst.append(n % base)
#     n = n // base
# print(lst.count(4))


#3 в 16 сс посчитать сколько цифр
# n = 2**51 + 2**40 + 2**35 + 2**17 - 2**5
# print(set(hex(n)[2:])) #ответ 5. считаем всё множество


#4
# n = 256**2 + 4096**16 - 15
# print(hex(n)[2:].count("f"))


#5
# for i in range(2, 11):
#     n = 559
#     lst = []
#     while n > 0:
#         lst.append(n % i)
#         n = n // i
#     print(sum(lst), i)


#6  другой прототип
# for x in range(0, 10):
#     a = f"4c{x}4"
#     b = f"{x}62a"
#     result = int(a, 15) + int(b, 13)
#     if result % 121 == 0:
#         print(result / 121)


#7
# for x in range(0, 16):
#     a = 4 + 8 * 19**1 + x * 19**2 + 2 * 19**3
#     b = x + 3 * 16 + 11 * 16**2 + 2 * 16**3
#     if (a + b) % 88 == 0:
#         print((a + b) / 88)


#8
# for x in range(0, 108):
#     a = 1 + 5 * 109 + 7 * 109**2 + x * 109**3
#     b = x + 7 * 215 + 3 * 215**2 + 2 * 215**3
#     if (a + b) % 567 == 0:
#         print((a + b) / 567)