#1
# def f(x, y):
#     if x == y: return 1
#     if x > y or x % 10 == 7: return 0
#     else:
#         return f(x + 1, y) + f(x + 7, y)
# print(f(1, 61))


#2
# def f(x, y):
#     if x == y: return 1
#     if x > y or x == 17: return 0
#     else:
#         return f(x + 2, y) + f(x + 3, y) + f(x * 2, y)
# print(f(3, 10) * f(10, 25))


#3
# def f(x, y):
#     if x == y: return 1
#     if x < y or x == 9 or x == 16: return 0
#     else:
#         return f(x - 1, y) + f(x - 2, y) + f(x // 3, y)
# print(f(19, 3))


#4
# def f(x, y):
#     if x == y: return 1
#     if x > y: return 0
#     else:
#         return f(x + 1, y) + f(x + 2, y) + f(x + 3, y)
# print(f(5, 7) * f(7, 11))


#5
# def f(x, y):
#     if x == y: return 1
#     if x > y or x == 35: return 0
#     else:
#         return f(x + 1, y) + f(x + 2, y) + f(x * 2, y)
# print(f(7, 13) * f(13, 15) * f(15, 51))


#6  прототип с количеством команд
# lst = []
# def f(x, step):
#     if step == 0: lst.append(x)
#     else:
#         f(x + 2, step - 1)
#         f(x + 3, step - 1)
#         f(x * 2, step - 1)
# f(10, 5)
# print(len(set(lst)))


#7  траектория не содержит простые числа
# def isPrime(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# def f(x, y):
#     if x == y: return 1
#     if x > y or isPrime(x): return 0
#     else:
#         return f(x + 1, y) + f(x + 2, y) + f(x * 3, y)
# print(f(8, 16) * f(16, 32))


#8
# for a in range(1, 101):
#     for c in range(1, 101):
#         f = ((5 + 3 + c) * a + c + 3) * a + c
#         if f == 329:
#             print(a + c)