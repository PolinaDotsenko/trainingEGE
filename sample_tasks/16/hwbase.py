#1
# def f(n):
#     if n < 3: return 2 * n
#     if n >= 3 and n % 2 == 0: return 3 * n + 5 + f(n - 2)
#     if n >= 3 and n % 2 != 0: return n + 2 * f(n - 6)
# print(f(61))


#2
# def f(n): 
#     if n < 1: return n
#     if n >= 1 and n % 2 == 0: return n + 3 * f(n - 3)
#     if n >= 1 and n % 2 != 0: return 5 * n + 2 * f(n - 5)
# print(f(30))


#3
# def f(n):
#     if n == 1: return 1
#     if n > 1 and n % 2 == 0: return 2 * f(n - 1)
#     if n > 1 and n % 2 != 0: return 5 * n + f(n - 2)
# print(f(64))


#4
# def f(n):
#     if n <= 3: return n
#     if n > 3 and n % 2 == 0: return 2 * n + f(n - 1)
#     if n > 3 and n % 2 != 0: return n * n + f(n - 2)

# s = len([n for n in range(1, 101) if f(n) % 3 == 0])
# print(s)


#5
# def F(n):
#     if n > 2: return F(n - 1) + G(n - 2)
#     else: return n

# def G(n):
#     if n > 2: return G(n - 1) + F(n - 2)
#     else: return n + 1

# print(F(6))