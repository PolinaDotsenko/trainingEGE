#3
# a = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 4 <= x <= 15
#     q = 12 <= x <= 20
#     f = (p and q) <= a
#     if f != f_usl:
#         print(x)    #15 - 12 = 3


#4
# a = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 130 <= x <= 171
#     q = 150 <= x <= 185
#     f = p <= ((q and (not a)) <= (not p))
#     if f != f_usl:
#         print(x)    #171 - 150 = 21


#1
# a = 1   #тк ищем наибольшее 
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 5 <= x <= 30
#     q = 14 <= x <= 23
#     f = (p == q) <= (not a)
#     if f == f_usl:
#         print(x)    #от 5 до 14 и от 23 до 30
#         #14 - 5 = 9     30 - 23 = 7     ответ 9


#2
# a = 1
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 10 <= x <= 29
#     q = 13 <= x <= 18
#     f = (a <= p) or q
#     if f == f_usl:
#         print(x)    #29 - 10 = 19


#5
# a = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 20 <= x <= 50
#     q = 30 <= x <= 65
#     f = (not a) <= (p <= (not q))
#     if f != f_usl:
#         print(x)


#6
# a = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 17 <= x <= 46
#     q = 22 <= x <= 57
#     f = (not a) <= ((p and q) <= a)
#     if f != f_usl:
#         print(x)


#7
# a = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 17 <= x <= 40
#     q = 20 <= x <= 57
#     f = (not a) <= ((p and q) <= a)
#     if f != f_usl:
#         print(x)


#8
# a = 0
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 10 <= x <= 40
#     q = 5 <= x <= 15
#     r = 35 <= x <= 50
#     f = (a or p) or (q <= r)
#     if f != f_usl:  #наименьшее
#         print(x)


#HOMEWORK
#1
# a = 0
# f_usl = 1
# for x in[k * 0.25 for k in range(-10000, 10000)]:
#     p = 22 <= x <= 72
#     q = 42 <= x <= 102
#     f = (not((not a) and p)) or q
#     if f != f_usl:
#         print(x)


#2
# a = 0
# f_usl = 1
# for x in[k * 0.25 for k in range(-10000, 10000)]:
#     p = 12 <= x <= 62
#     q = 52 <= x <= 92
#     f = (not((not a) and p)) or q
#     if f != f_usl:
#         print(x)


#3
# a = 1
# f_usl = 1
# for x in[k * 0.25 for k in range(-10000, 10000)]:
#     p = 3 <= x <= 38
#     q = 21 <= x <= 57
#     f = (q <= p) <= (not a)
#     if f == f_usl:
#         print(x)


#4
# a = 1
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 1 <= x <= 39
#     q = 23 <= x <= 58
#     f = (p <= (not q)) <= (not a)
#     if f == f_usl:
#         print(x)


#5
# a = 1
# f_usl = 1
# for x in [k * 0.25 for k in range(-10000, 10000)]:
#     p = 3 <= x <= 13
#     q = 12 <= x <= 22
#     f = (a <= p) or q
#     if f == f_usl:
#         print(x)