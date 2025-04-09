#2  !!!
# def f(a, x, y):
#     return ((x < 6) <= (x * x < a)) and ((y * y <= a) <= (y <= 6))

# c = 0
# for a in range(-300, 300):
#     if all(f(a, x, y) == 1 for x in range(0, 300) for y in range(0, 300)):
#         c += 1
# print(c)


#3
# def f(a, x, y):
#     return (y + 2 * x < a) or (x > 30) or (y > 20)

# for a in range(0, 300):
#     if all(f(a, x, y) for x in range(0, 300) for y in range(0, 300)):
#         print(a)
#         break


#4
# def f(a, x, y):
#     return (y + 2 * x != 48) or (a < x) or (x < y)

# for a in range(0, 300):
#     if all(f(a, x, y) for x in range(0, 300) for y in range(0, 300)):
#         print(a)


#5  !!!
# def f(a, x):
#     return (x & 29 != 0) <= ((x & 17 == 0) <= (x & a != 0))

# for a in range(0, 300):
#     if all(f(a, x) for x in range(0, 300)):
#         print(a)
#         break


#6
# def f(a, x):
#     return (x & 25 != 0) <= ((x & 17 == 0) <= (x & a != 0))

# for a in range(0, 300):
#     if all(f(a, x) for x in range(0, 300)):
#         print(a)
#         break


#7
# def f(a, x):
#     return (x & 25 != 0) <= ((x & 9 == 0) <= (x & a != 0))

# for a in range(0, 300):
#     if all(f(a, x) for x in range(0, 300)):
#         print(a)
#         break


#8  !!!
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return (not d(x, a)) <= (d(x, 6) <= (not d(x, 4)))

# for a in range(1, 300): #a натуральное 
#     if all(f(a, x) for x in range(1, 300)): #x натуральное
#         print(a)


#9
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return (a < 50) and ((not d(x, a)) <= (d(x, 10) <= (not d(x, 12))))

# for a in range(1, 300):
#     if all(f(a, x) == 1 for x in range(1, 300)):
#         print(a)


#10
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return d(120, a) and (d(x, 36)) <= ((not d(x, a)) <= (not d(x, 45)))

# for a in range(1, 300):
#     if all(f(a, x) == 1 for x in range(1, 300)):
#         print(a)