#1      base
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return d(144, a) and ((not d(x, a)) <= (d(x, 18) <= (not d(x, 24)))) 

# for a in range(1, 400):
#     if all(f(a, x) for x in range(1, 400)):
#         print(a)


#2
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return d(70, a) and ((not d(x, a)) <= (d(x, 35) <= (not d(x, 63))))

# for a in range(1, 400):
#     if all(f(a, x) for x in range(1, 400)):
#         print(a)


#3
# def f(a, x, y):
#     return (x * y < 140) or (y > a) or (x > a)

# for a in range(0, 400):
#     if all(f(a, x, y) for x in range(0, 400) for y in range(0, 400)):
#         print(a)


#4
# def f(a, x, y):
#     return (2 * x + 3 * y < a) or (x > y) or (y > 24)

# for a in range(0, 400):
#     if all(f(a, x, y) for x in range(0, 400) for y in range(0, 400)):
#         print(a)
#         break


#5
# def f(a, x):
#     return (x & 51 == 0) or ((x & 41 == 0) <= (x & a == 0))

# for a in range(0, 400):
#     if all(f(a, x) for x in range(0, 400)):
#         print(a)
#         break


#1      pro
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return d(a, 7) and (d(240, x) <= ((not d(a, x)) <= (not d(780, x))))

# cnt = 0
# for a in range(1, 1001):
#     if all(f(a, x) for x in range(1, 1001)):
#         cnt += 1
# print(cnt)


#2
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return d(a, 12) and (d(530, x) <= ((not d(a, x)) <= (not d(170, x))))

# cnt = 0
# for a in range(1, 1001):
#     if all(f(a, x) for x in range(1, 1001)):
#         cnt += 1
# print(cnt)


#3
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return d(a, 35) and (d(730, x) <= ((not d(a, x)) <= (not d(110, x))))

# for a in range(1, 1001):
#     if all(f(a, x) for x in range(1, 1001)):
#         print(a)
#         break
