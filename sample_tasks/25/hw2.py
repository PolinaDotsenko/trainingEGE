#1
# def f(n):
#     lst = []
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(489_421, 489_441):
#     if len(f(i)) == 4:
#         print(f(i))


#2
# def f(n):
#     lst = []
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(123456789, 223456790):
#     if len(f(i)) == 3:
#        print(i, max(f(i)))


#3
# def f(n):
#     lst = []
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(312614, 312652):
#     if len(f(i)) == 6:
#         print(f(i))


#4
# from fnmatch import *

# for i in range(273, 10**8 + 1, 273):
#     n = fnmatch(str(i), "12??36*1")
#     if n == True:
#         print(i, i // 273)


#5
# from fnmatch import *

# for i in range(317, 10**8 + 1, 317):
#     n = fnmatch(str(i), "12??1*56")
#     if n == True:
#         print(i, i // 317)


#6
# from fnmatch import *

# for i in range(4891, 10**10 + 1, 4891):
#     n = fnmatch(str(i), "1?2711*0")
#     if n == True:
#         print(i)