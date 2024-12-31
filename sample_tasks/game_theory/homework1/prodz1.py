#1
# def f(s, n):
#     if s >= 38: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 1, n - 1), f(s + 2, n - 1), f(s + 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 38) if f(s, 2)])
# print(min([s for s in range(1, 38) if not f(s, 1) and f(s, 3)]), max([s for s in range(1, 38) if not f(s, 1) and f(s, 3)]))
# print([s for s in range(1, 38) if not f(s, 2) and f(s, 4)])


#2
# def f(s, n):
#     if s >= 50: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print(min([s for s in range(1, 50) if f(s, 2)]))
# print(len([s for s in range(1, 50) if not f(s, 1) and f(s, 3)]))
# print([s for s in range(1, 50) if not f(s, 2) and f(s, 4)])


#3
# def f(s, n):
#     if s >= 30: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s + 3, n - 1), f(s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print(min([s for s in range(1, 30) if f(s, 2)]))
# print(len([s for s in range(1, 30) if not f(s, 1) and f(s, 3)]))
# print([s for s in range(1, 30) if not f(s, 2) and f(s, 4)])