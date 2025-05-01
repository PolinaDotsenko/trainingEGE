#1
# def f(a, s, n):
#     if a + s >= 231: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 2, s, n - 1), f(a, s + 2, n - 1), f(a * 2, s, n - 1), f(a, s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print(max([s for s in range(1, 214) if f(17, s, 2)]))
# print([s for s in range(1, 214) if not f(17, s, 1) and f(17, s, 3)])
# print([s for s in range(1, 214) if not f(17, s, 2) and f(17, s, 4)])


#2
# def f(a, s, n):
#     if a + s >= 259: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 2, s, n - 1), f(a, s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 242) if f(17, s, 2)])
# print([s for s in range(1, 242) if not f(17, s, 1) and f(17, s, 3)])
# print([s for s in range(1, 242) if not f(17, s, 2) and f(17, s, 4)])


#3
# def f(a, s, n):
#     if a + s >= 133: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 4, s, n - 1), f(a, s * 4, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 126) if f(7, s, 2)])
# print([s for s in range(1, 126) if not f(7, s, 1) and f(7, s, 3)])
# print([s for s in range(1, 126) if not f(7, s, 2) and f(7, s, 4)])


#4
# def f(a, s, n): 
#     if a + s >= 259: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 2, s, n - 1), f(a, s * 2, n - 1)]
#     return any(h) if (n - 1)% 2 == 0 else all(h)

# print([s for s in range(1, 242) if f(17, s, 2)])
# print([s for s in range(1, 242) if not f(17, s, 1) and f(17, s, 3)])
# print([s for s in range(1, 242) if not f(17, s, 2) and f(17, s, 4)])


#5  ограничение сверху
def f(a, s, n): 
    if 40 <= a + s <= 49: return n % 2 == 0
    if a + s > 49: return n % 2 != 0
    if n == 0: return 0
    h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 2, s, n - 1), f(a, s * 2, n - 1)]
    return any(h) if (n - 1)% 2 == 0 else all(h)

print([s for s in range(1, 26) if f(14, s, 2)])
print([s for s in range(1, 26) if not f(14, s, 1) and f(14, s, 3)])
print([s for s in range(1, 26) if not f(14, s, 2) and f(14, s, 4)])