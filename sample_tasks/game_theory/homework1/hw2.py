#1
# def f(s, n):
#     if s >= 108: return n % 2 == 0
#     if n == 0: return 0
#     if s % 2 != 0:
#         h = [f(s + 1, n - 1), f(s * 2, n - 1)]
#     if s % 2 == 0: 
#         h = [f(s + 1, n - 1), f(s * 1.5, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print(max([s for s in range(1, 108) if not f(s, 1) and f(s, 2)]))    #1
# print([s for s in range(1, 108) if not f(s, 1) and f(s, 3)])    #2
# print(max([s for s in range(1, 108) if not f(s, 2) and f(s, 4)]))    #3


#2
# def f(s, n):
#     if s >= 47: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 1, n - 1), f(s + 2, n - 1), f(s * 2, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 47) if not f(s, 1) and f(s, 2)]) #4
# print([s for s in range(1, 47) if not f(s, 1) and f(s, 3)]) #5
# print([s for s in range(1, 47) if not f(s, 2) and f(s, 4)]) #6


#3
# def f(s, n):
#     if s >= 89: return n % 2 == 0
#     if n == 0: return 0
#     h = [f(s + 2, n - 1), f(s + 3, n - 1), f(s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)

# print([s for s in range(1, 89) if not f(s, 1) and f(s, 2)]) #7
# print([s for s in range(1, 89) if not f(s, 1) and f(s, 3)]) #8
# print([s for s in range(1, 89) if not f(s, 2) and f(s, 4)]) #9


#4
def f(s, n):
    if s >= 96: return n % 2 == 0
    if n == 0: return 0
    if s % 2 == 0:
        h = [f(s + 1, n - 1), f(s + (s // 2), n - 1)]
    if s % 3 == 0:
        h = [f(s + 1, n - 1), f(s + (s // 3), n - 1)]
    if s % 2 != 0 and s % 3 != 0:
        h = [f(s + 1, n - 1), f(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 96) if not f(s, 1) and f(s, 2)]) #10
print([s for s in range(1, 96) if not f(s, 1) and f(s, 3)]) #11
print([s for s in range(1, 96) if not f(s, 2) and f(s, 4)]) #12