#1 3 вопрос мимо
def f(a, s, n):
    if 60 <= a + s <= 79: return n % 2 == 0
    if s > 79: return n % 2 != 0
    if n == 0: return 0
    h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 3, s, n - 1), f(a, s * 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 52) if not f(8, s, 1) and f(8, s, 2)])
print(len([s for s in range(1, 52) if not f(8, s, 1) and f(8, s, 3)]))
print([s for s in range(1, 52) if not f(8, s, 2) and f(8, s, 4)])


#2 правильно
# def f(a, s, n):
#     if a + s >= 90: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 3, s, n - 1), f(a, s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 81) if f(9, s, 2)])
# print(len([s for s in range(1, 81) if not f(9, s, 1) and f(9, s, 3)]))
# print([s for s in range(1, 81) if f(9, s, 2) or f(9, s, 4) or f(9, s, 6)])


#3 правильно
# def f(a, s, n):
#     if a + s >= 73: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a + s, s, n - 1), f(a, s + a, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 64) if f(9, s, 2)])
# print([s for s in range(1, 64) if not f(9, s, 1) and f(9, s, 3)])
# print([s for s in range(1, 64) if not f(9, s, 2) and f(9, s, 4)])


#4 правильно
# def f(a, s, n):
#     if a + s >= 125: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 4, s, n - 1), f(a, s * 4, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 118) if f(7, s, 2)])
# print([s for s in range(1, 118) if not f(7, s, 1) and f(7, s, 3)])
# print([s for s in range(1, 118) if not f(7, s, 2) and f(7, s, 4)])

