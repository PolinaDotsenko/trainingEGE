#1
# def f(a, s, n):
#     if 60 <= a + s <= 79: return n % 2 == 0
#     if a + s > 79: return n % 2 != 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1),
#          f(a * 3, s, n - 1), f(a, s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 52) if f(8, s, 2)])
# print([s for s in range(1, 52) if not f(8, s, 1) and f(8, s, 3)])
# print([s for s in range(1, 52) if not f(8, s, 2) and f(8, s, 4)])


#2  "при котором это возможно" ---> any()
# def f(a, s, n):
#     if a + s >= 90: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1),
#           f(a * 3, s, n - 1), f(a, s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 81) if f(9, s, 2)])
# print([s for s in range(1, 81) if not f(9, s, 1) and f(9, s, 3)])
# print([s for s in range(1, 81) if f(9, s, 6)])


#3
# def f(a, s, n):
#     if a + s >= 73: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a + s, s, n - 1), f(a, s + a, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 64) if f(9, s, 2)])
# print([s for s in range(1, 64) if not f(9, s, 1) and f(9, s, 3)])
# print([s for s in range(1, 64) if not f(9, s, 2) and f(9, s, 4)])


#4
# def f(s, n):
#     if s >= 50: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 50) if f(s, 2)])
# print([s for s in range(1, 50) if not f(s, 1) and f(s, 3)])
# print([s for s in range(1, 50) if not f(s, 2) and f(s, 4)])