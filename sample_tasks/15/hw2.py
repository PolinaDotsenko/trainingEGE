#1
# def f(a, x, y):
#     return (3 * x + 2 * y > 25) or (x > 2 * y) or (x + 4 * y < a)

# for a in range(-500, 500):
#     # for x in range(0, 500):
#     #     for y in range(0, 500):
#     #         if f(a, x, y) == 0:
#     if any(f(a, x, y) == 0 for x in range(0, 300) for y in range(0, 300)):
#                 print(a)


#2
# def f(a, x, y):
#     return (12 * x + 2 * y > 56) or (x > 2 * y) or (5 * x + y < a)

# for a in range(-300, 300):
#     if any(f(a, x, y) == 0 for x in range(0, 300) for y in range(0, 300)):
#         print(a)


#3
# def f(a, x):
#     return ((x & 673 != 0) or (x & 189 != 0)) <= (x & a > 0)

# for a in range(1, 800):
#     if all(f(a, x) == 1 for x in range(0, 800)):
#         print(a)


#4
# def f(a, x, y):
#     return ( x * y < a) or (x < y) or (9 < x)

# for a in range(0, 300):
#     if all(f(a, x, y) == 1 for x in range(0, 300) for y in range(0, 300)):
#         print(a)
#         break


#5
# def f(a, x, y):
#     return (x < a) or (y < a) or (x + 2 * y > 50)

# for a in range(0, 300):
#     if all(f(a, x, y) == 1 for x in range(0, 300) for y in range(0, 300)):
#         print(a)
#         break
    

#6
# def f(a, x, y):
#     return (7 * y + 5 * x < 1000) or (x < y) or (a < x)

# for a in range(0, 300):
#     if all(f(a, x, y) == 1 for x in range(0, 300) for y in range(0, 300)):
#         print(a)


#7
# def f(a, x, y):
#     return ((3 * x + 2 * y) > 25) or (x > 2 * y) or ((x + 4 * y) < a)

# for a in range(-300, 300):
#     if any(f(a, x ,y) == 0 for x in range(0, 300) for y in range(0, 300)):
#         print(a)


#8
# def f(a, x, y):
#     return ((12 * x + 2 * y) > 56) or (x > (2 * y)) or ((5 * x + y) < a)

# for a in range(-1000, 1000):
#     if any(f(a, x, y) == 0 for x in range(0, 1000) for y in range(0, 1000)):
#         print(a)


#9
# def f(a, x):
#     return ((x & 673 != 0) or (x & 189 != 0)) <= (x & a > 0)

# for a in range(1, 1000):
#     if all(f(a, x) == 1 for x in range(0, 1000)):
#         print(a)


#10
# def f(a, x, y):
#     return (x * y < a) or (x < y) or (9 < x)

# for a in range(0, 1000):
#     if all(f(a, x, y) == 1 for x in range(0, 1000) for y in range(0, 1000)):
#         print(a)
#         break


#11
# def f(a, x ,y):
#     return (x < a) or (y < a) or (x + 2 * y > 50)

# for a in range(0, 1000):
#     if all(f(a, x, y) == 1 for x in range(0, 1000) for y in range(0, 1000)):
#         print(a)
#         break


#12
# def f(a, x, y):
#     return (7 * y + 5 * x < 1000) or (x < y) or (a < x)

# for a in range(0, 1000):
#     if all(f(a, x, y) == 1 for x in range(0, 1000) for y in range(0, 1000)):
#         print(a)


#отрезки
#1
# from itertools import *

# def f(x):
#     p = 5 <= x <= 30
#     q = 14 <= x <= 23
#     a = a1 <= x <= a2
#     return (p == q) <= (not a)

# lst = []
# ox = [i / 4 for i in range(4*4, 31*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(max(lst))


#2
# from itertools import *

# def f(x):
#     p = 10 <= x <= 29
#     q = 13 <= x <= 18
#     a = a1 <= x <= a2
#     return (a <= p) or q

# lst = []
# ox = [i / 4 for i in range(9*4, 30*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(max(lst))


#3
# from itertools import *

# def f(x):
#     p = 4 <= x <= 15
#     q = 12 <= x <= 20
#     a = a1 <= x <= a2
#     return (p and q) <= a

# lst = []
# ox = [i / 4 for i in range(3*4, 21*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))


#4
# from itertools import *

# def f(x):
#     p = 10 <= x <= 15
#     q = 10 <= x <= 20
#     r = 5 <= x <= 15
#     a = a1 <= x <= a2
#     return (a <= p) == (q <= r)

# lst = []
# ox = [i / 4 for i in range(4*4, 21*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))


#5
# from itertools import *

# def f(x):
#     p = 3 <= x <= 38
#     q = 21 <= x <= 57
#     a = a1 <= x <= a2
#     return (q <= p) <= (not a)

# lst = []
# ox = [i / 4 for i in range(2*4, 58*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(max(lst))


#6
# from itertools import *

# def f(x):
#     p = 10 <= x <= 21
#     q = 13 <= x <= 38
#     r = 18 <= x <= 25
#     a = a1 <= x <= a2
#     return (not (q <= (p or r))) <= ((not a) <= (not q))

# lst = []
# ox = [i / 4 for i in range(9*4, 39*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))


#7
# from itertools import *

# def f(x):
#     p = 8 <= x <= 39
#     q = 23 <= x <= 58
#     a = a1 <= x <= a2
#     return (p or a) <= (q or a)

# lst = []
# ox = [i / 4 for i in range(7*4, 59*4)]
# for a1, a2 in combinations(ox, 2):
#     if all(f(x) == 1 for x in ox):
#         lst.append(a2 - a1)
# print(min(lst))