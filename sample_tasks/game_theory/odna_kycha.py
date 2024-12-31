#1 (код почти неизменен для решения любых таких задач)
# def f(s, n):
#     if s >= 74:
#         return n % 2 == 0
#     if n == 0:
#         return 0
#     h = [f(s + 1, n - 1), f(s + 2, n - 1), f(s * 3, n - 1)]
#     return any(h) if (n - 1) % 2 == 0 else all(h)   #для №19 меняем all на any если нужно

# print([s for s in range(1, 74) if f(s, 2)]) #19 
# print([s for s in range(1, 74) if not f(s, 1) and f(s, 3)]) #20
# print([s for s in range(1, 74) if not f(s, 2) and f(s, 4)]) #21


#2
def f(s, n):
    if s >= 52: return n % 2 == 0
    if n == 0: return 0
    h = [f(s + 1, n - 1), f(s + 4, n - 1), f(s * 2, n - 1)]
    return any(h) if (n - 1) % 2 == 0 else all(h)

print([s for s in range(1, 52) if f(s, 2)]) #19
print([s for s in range(1, 52) if not f(s, 1) and f(s, 3)]) #20
print([s for s in range(1, 52) if not f(s, 2) and f(s, 4)]) #21











