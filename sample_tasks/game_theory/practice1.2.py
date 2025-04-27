#1
# def f(s, n):
#     if s >= 25: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 25) if not f(s, 1) and f(s, 2)])
# print([s for s in range(1, 25) if not f(s, 1) and f(s, 3)])
# print([s for s in range(1, 25) if not f(s, 2) and f(s, 4)])


#2
# def f(s, n):
#     if s >= 30: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s + 3, n - 1), f(s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 30) if f(s, 2)])
# print([s for s in range(1, 30) if not f(s, 1) and f(s, 3)])
# print([s for s in range(1, 30) if not f(s, 2) and f(s, 4)])


#3
# def f(s, n):
#     if s >= 82: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s + 4, n - 1), f(s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 82) if f(s, 2)])     #any(после неудачного хода Пети)
# print([s for s in range(1, 82) if not f(s, 1) and f(s, 3)])     #all(независимо от игры противника)
# print([s for s in range(1, 82) if not f(s, 2) and f(s, 4)])     #all(при любой игре противника)