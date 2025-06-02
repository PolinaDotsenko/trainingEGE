# 12
# def f(s, a, c, m):
#     if s + a >= 66: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s + 2, a, c + 1, m), f(s, a + 2, c + 1, m), f(s*2, a, c + 1, m), f(s, a*2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)

# for s in range(1, 59):
#     for m in range(1, 5):
#         if f(s, 7, 0, m) == True:
#             print(s, m)
#             break

# 13
# def f(s, a, c, m):
#     if s + a <= 20: return c % 2 == m % 2
#     if c == m: return 0
#     h = [f(s - 1, a, c + 1, m), f(s, a - 1, c + 1, m), f((s + 1) // 2, a, c + 1, m), f(s, (a + 1) //2, c + 1, m)]
#     return any(h) if (c + 1) % 2 == m % 2 else all(h)

# for s in range(11, 50):
#     for m in range(1, 5):
#         if f(s, 10, 0, m) == True:
#             print(s, m)
#             break

# 1
# def f(A, x, y):
#     return (x**2 - 3*x + 2 > 0) or (y > x**2 + 7) or (x*y < A)

# for A in range(0, 500):
#     if all(f(A, x, y) == True for x in range(1, 250) for y in range(1, 250)):
#         print(A)
#         break

# 3
# def f(A, x, y):
#     return (x**2 - 11*x + 28 > 0) or (y**2 - 9 * y + 14 > 0) or (x**2 + y**2 > A)

# for A in range(0, 500):
#     if all(f(A, x, y) == True for x in range(1, 250) for y in range(1, 250)):
#         print(A)

# 4
# def f(A, x, y):
#     return ((x - 20 < A) and (20 - x < A)) or (x*y > 50)

# for A in range(0, 500):
#     if all(f(A, x, y) == True for x in range(1, 250) for y in range(1, 250)):
#         print(A)
#         break

# 7
# def f(A,x):
#     return (x & 13 == 0) <= ((x & 40 != 0) <= (x & A != 0))

# for A in range (0,500):
#     if all(f(A,x)== True for x in range (1,250)):
#         print (A)
#         break

# 12
# def d(n, m):
#     return n % m == 0

# def f(A,x):
#     return (not(d(x, 16) == d(x, 24))) <= d(x, A)

# for A in range(1, 1000):
#     if all(f(A,x) == True for x in range(1,1000)):
#         print(A)

# 13
# def d(n, m):
#     return n // m

# def f(A,x):
#     return (d(x, 50) > 3) or (not(d(x,13) > 3) or (d(x, A) > 6))

# for A in range(1, 1000):
#     if all(f(A,x) == True for x in range(1,1000)):
#         print(A)

# 14
# def d(n, m):
#     return n % m == 0

# def f(A,x):
#     return d(x, A) and (A < 10) or (not d(x, 44)) and (not d(x, 99)) and (A < 10)

# for A in range(1, 1000):
#     if all(f(A,x) == True for x in range(1,1000)):
#         print(A)
        
# def Del(n,m):
#     return n % m == 0
# def f(A,x):
#     return (Del(x, A) and (not Del(x, 50))) <= ((not Del(x, 18)) or Del(x, 50))

# for A in range (1,500):
#     if all(f(A,x)== True for x in range (1,1000)):
#         print (A)
#         break



