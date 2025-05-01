#1
# def f(a, s, n):
#     if (a + s) >= 77: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 2, s, n - 1), f(a, s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 70) if f(7, s, 2)])
# print([s for s in range(1, 70) if not f(7, s, 1) and f(7, s, 3)])
# print([s for s in range(1, 70) if not f(7, s, 2) and f(7, s, 4)])


#2
# def f(a, s, n):
#     if (a + s) >= 82: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 4, s, n - 1), f(a, s * 4, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 78) if f(4, s, 2)])
# print([s for s in range(1, 78) if not f(4, s, 1) and f(4, s, 3)])
# print([s for s in range(1, 78) if not f(4, s, 2) and f(4, s, 4)])


#3
# def f(a, s, n):
#     if a + s >= 41: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s + 2, n - 1), f(a + 2, s + 1, n - 1), f(a * 2, s, n - 1), f(a, s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 33) if f(8, s, 2)])
# print([s for s in range(1, 33) if not f(8, s, 1) and f(8, s, 3)])
# print([s for s in range(1, 33) if not f(8, s, 2) and f(8, s, 4)])


#4  одна куча дострок
# def f(s, n):
#     if s <= 87: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s - 2, n - 1), f(s // 2, n - 1)] 
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(88, 300) if f(s, 2)])
# print([s for s in range(88, 300) if not f(s, 1) and f(s, 3)])
# print([s for s in range(88, 300) if not f(s, 2) and f(s, 4)])