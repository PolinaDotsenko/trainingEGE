#1
# def f(a, s, n):
#     if a + s >= 45: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 3, s, n - 1), f(a, s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 41) if f(4, s, 2)])      #all на any
# print([s for s in range(1, 41) if not f(4, s, 1) and f(4, s, 3)])
# print([s for s in range(1, 41) if not f(4, s, 2) and f(4, s, 4)])


