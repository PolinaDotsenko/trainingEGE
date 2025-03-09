#1 
# from fnmatch import *

# for i in range(51, 10**6 + 1, 51):
#     if fnmatch(str(i), "12*45*"):
#         print(i, i // 51)


#2
# from fnmatch import *

# for i in range(169, 10**9 + 1, 169):
#     if fnmatch(str(i), "123*567?"):
#         print(i, i // 169)


#3 
from fnmatch import *

for i in range(17, 10**9 + 1, 17):
    if fnmatch(str(i), "1?34567?9"):
        print(i, i // 17)


#4
# def d(n):
#     lst = []
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // 1)
#     return sorted(set(lst))

# def isPrime(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n // i == 0:
#             return False
#     return True

# p = []
# for i in range(450001, 450101):
#     n = d(i)
#     if len(n) > 0:
#         for x in n:
#             if isPrime(x):
#                 p.append(x)
#         m = max(p) - min(p)
#         if m % 29 == 11:
#             print(m)