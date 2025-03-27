#1
# def f(s, n):
#     if s >= 25: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 25) if f(s, 2)]) #7
# print([s for s in range(1, 25) if not f(s, 1) and f(s, 3)]) #3
# print([s for s in range(1, 25) if not f(s, 2) and f(s, 4)]) #78


#2
# def f(s, n):
#     if s >= 50: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 50) if f(s, 2)]) 
# print([s for s in range(1, 50) if not f(s, 1) and f(s, 3)]) 
# print([s for s in range(1, 50) if not f(s, 2) and f(s, 4)]) 