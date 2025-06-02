#1
# def f(x, y):
#     if x == y: return 1
#     if x < y: return 0
#     else:
#         return f(x - 2, y) + f(x // 2, y)
# print(f(38, 16) * f(16, 2))


#2
# def f(x, y):
#     if x == y: return 1
#     if x < y: return 0
#     else:
#         return f(x - 2, y) + f(x // 2, y)
# print(f(30, 14) * f(14, 1))


#3
# def f(x, y):
#     if x == y: return 1
#     if x > y: return 0
#     else:
#         return f(x + 1, y) + f(x + 2, y) + f(x + 3, y)
# print(f(1, 7) * f(7, 35))


#4
# def f(x, y):
#     if x == y: return 1
#     if x > y: return 0
#     else:
#         return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
# print(f(4, 11) * f(11, 13) * f(13, 15))


#5
# def f(x, y):
#     if x == y: return 1
#     if x < y: return 0
#     else:
#         return f(x - 1, y) + f(x // 2, y)
# print(f(78, 16)* f(16, 4))


#6
# def f(x, y):
#     if x == y: return 1
#     if x < y: return 0
#     else:
#         return f(x - 1, y) + f(x // 3, y)
# print(f(67, 33) * f(33, 5))


#7
# def f(x, y):
#     if x == y: return 1
#     if x > y: return 0
#     else:
#         return f(x + 2, y) + f(x * 2, y)
# print(f(1, 18) * f(18, 52))


#8
def f(x, y):
    if x == y: return 1
    if x > y: return 0
    else:
        return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)
print(f(1, 10) * f(10, 15))