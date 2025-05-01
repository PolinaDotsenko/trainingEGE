# #1  ограничение сверху
# def f(s, n):
#     if 65 <= s <= 100: return n % 2 == 0    #!
#     if s > 100: return n % 2 != 0   #!
#     if n == 0: return 0
#     h = [f(s + 1, n - 1), f(s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 65) if f(s, 2)])
# print([s for s in range(1, 65) if not f(s, 1) and f(s, 3)])
# print([s for s in range(1, 65) if not f(s, 2) and f(s, 4)])


#2  просто большие числа
# def f(s, n):
#     if s >= 1000: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 100, n - 1), f(s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print(len([s for s in range(1, 1000) if f(s, 2)]))
# print(len([s for s in range(1, 1000) if not f(s, 1) and f(s, 3)]))
# print([s for s in range(1, 1000) if not f(s, 2) and f(s, 4)])


#3  округление в большую сторону (s + 1) // 2 или  from math func ceil()
# def f(a, s, n):
#     if a + s <= 32: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a - 1, s, n - 1), f(a, s - 1, n - 1), f((a + 1) // 2, s, n - 1), f(a, (s + 1) // 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(23, 150) if f(10, s, 2)])
# print([s for s in range(23, 150) if not f(10, s, 1) and f(10, s, 3)])
# print([s for s in range(23, 150) if not f(10, s, 2) and f(10, s, 4)])


#4  три кучи
# def f(a, b, s, n):
#     if a + b + s >= 71: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 3, b, s, n - 1), f(a, b + 3, s, n - 1), f(a, b, s + 3, n - 1), 
#         f(a * 2, b, s, n - 1), f(a, b * 2, s, n - 1), f(a, b, s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 59) if f(7, 5, s, 2)])
# print([s for s in range(1, 59) if not f(7, 5, s, 1) and f(7, 5, s, 3)])
# print([s for s in range(1, 59) if not f(7, 5, s, 2) and f(7, 5, s, 4)])


#5  отслеживание ходов
# def f(s, n, p):
#     if s >= 68: return n % 2 == 0
#     if n == 0: return 0
#     if p == "":
#         h =[f(s + 1, n - 1, "+1"), f(s + 2, n - 1, "+2"), f(s * 2, n - 1, "*2")]
#     if p == "+1":
#         h =[f(s + 2, n - 1, "+2"), f(s * 2, n - 1, "*2")]
#     if p == "+2":
#         h =[f(s + 1, n - 1, "+1"), f(s * 2, n - 1, "*2")]
#     if p == "*2":
#         h =[f(s + 1, n - 1, "+1"), f(s + 2, n - 1, "+2")]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 68) if f(s, 2, "")])
# print([s for s in range(1, 68) if not f(s, 1, "") and f(s, 3, "")])
# print([s for s in range(1, 68) if not f(s, 2,"") and f(s, 4, "")])
