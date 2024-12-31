from itertools import product

#1
# def f(a, s, n):
#     if a + s >= 59: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(a + 1, s, n - 1), f(a, s + 1, n - 1), f(a * 2, s, n - 1), f(a, s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 54) if f(5, s, 2)])
# print([s for s in range(1, 54) if not f(5, s, 1) and f(5, s, 3)])
# print([s for s in range(1, 54) if not f(5, s, 2) and f(5, s, 4)])


#2
def f(a, s, n):
    if a >= 48 or s >= 48: return n % 2 == 0
    if n == 0: return 0
    if a > s:
        h = [f(a + 1, s, n - 1), f(a + 2, s, n - 1), f(a + 3, s, n - 1), f(a, s * 2, n - 1)]
    if s > a:
        h = [f(a, s + 1, n - 1), f(a, s + 2, n - 1), f(a, s + 3, n - 1), f(a * 2, s, n - 1)]
    if a == s:
        h = [f(a + 1, s, n - 1), f(a + 2, s, n - 1), f(a + 3, s, n - 1), f(a, s + 1, n - 1), f(a, s + 2, n - 1), f(a, s + 3, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print(min([a + s for a, s in product(range(1, 48), repeat=2) if f(a, s, 1)]))
print([s for s in range(1, 48) if not f(39, s, 1) and f(39, s, 3)])
print([s for s in range(1, 48) if not f(39, s, 2) and f(39, s, 4)])