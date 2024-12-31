#из теории
#1 тип
# def f(a, x, y):
#     return ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9)) #импликация(следует) = "<="

# for a in range(0, 500):
#     OK = True  #пример решения через флажок
#     for x in range(0, 500):
#         for y in range(0, 500):
#             if f(a, x, y) == False:
#                 OK = False
#                 break
#     if OK == True:
#         print(a)


#практика
#1 (1 type)
# def f(a, x, y):
#      return ((x <= 9) <= (x * x <= a)) and ((y * y <= a) <= (y <= 9)) #импликация(следует) = "<="

# for a in range(-300, 300):
#     if all(f(a, x, y) for x in range(0, 300) for y in range(0, 300)):
#          print(a)


#2
# def f(a, x, y):
#     return ((x < 6) <= (x ** 2 < a)) and ((y ** 2 <= a) <= (y <= 6))

# cnt = 0
# for a in range(-300, 300):
#     if all(f(a, x, y) for x in range(0, 300) for y in range(0, 300)):
#         cnt += 1
# print(cnt)


#3
# def f(a, x, y):
#     return (y + 2 * x <  a) or (x > 30) or (y > 20)

# for a in range(0, 400):
#     if all(f(a, x, y) for x in range(0, 400) for y in range(0, 400)):
#         print(a)
#         break


#4
# def f(a, x, y):
#     return (y + 2 * x != 48) or (a < x) or (x < y)

# for a in range(0, 400):
#     if all(f(a, x, y) for x in range(0, 400) for y in range(0, 400)):
#         print(a)


#5 (2 type. побитовая конъюнкция)
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


#8 (3 type. делители)
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return (not d(x, a)) <= (d(x, 6) <= (not d(x, 4)))

# for a in range(1, 300):
#     if all(f(a, x) for x in range(1, 300)):
#         print(a)


#9
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return (a < 50) and ((not d(x, a)) <= (d(x, 10) <= (not d(x, 12))))

# for a in range(1, 300):
#     if all(f(a, x) for x in range(1, 300)):
#         print(a)


#10
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return (a < 50) and ((not d(x, a)) <= (d(x, 10) <= (not d(x, 18))))

# for a in range(1, 300):
#     if all(f(a, x) for x in range(1, 300)):
#         print(a)


#11
# def d(n, m):
#     return n % m == 0

# def f(a, x):
#     return d(120, a) and (d(x, 36) <= ((not d(x, a)) <= (not d(x, 45))))

# for a in range(1, 300):
#     if all(f(a, x) for x in range(1, 300)):
#         print(a)