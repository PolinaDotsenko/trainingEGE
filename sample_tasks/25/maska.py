from fnmatch import *


#1 вводное
# def isPrime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# c = 1
# for i in range(3614033, 3614117):
#     n = isPrime(i)
#     if n: print(c, i)
#     c += 1


#2
    #!!!импортируем библиотеку(эта строчка есть в начале файла)
# for i in range(17, 10**9 + 1, 17):
#     if fnmatch(str(i), "1?34567?9"):
#         print(i, i // 17)


#5
#импорт
# for i in range(2025, 10**8 +1, 2025):
#     if fnmatch(str(i), "12*34?5"):
#         print(i, i // 2025)


#3
#импорт
# def isPrime(n):
#     for i in range(2, int(n*0.5) + 1):
#         if n % i == 0:
#             return False
#     return True

# for i in range(2627, 10**9 + 1, 2627):
#     s = sum([int(x) for x in str(i)])
#     if fnmatch(str(i), "7*53?3*1") and isPrime(s):
#         print(i, i // 2627)


#4 (прототип из первой практики)
# def d(n):
#     lst = []
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(350001, 350201):
#     n = d(i)
#     if len(n) > 0:
#         m = max(n) - min(n)
#         if m % 23 == 9:
#             print(i, m)