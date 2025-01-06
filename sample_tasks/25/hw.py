#1
# def d(n):
#     lst = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(95632, 95651):
#     n = d(i)
#     m = [x for x in n if x % 2 != 0]
#     if len(m) == 6:
#         print(m)


#2
# def d(n):
#     lst = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# m = []
# for i in range(84052, 84131):
#     n = d(i)
#     m.append([len(n), i])
# print(max(m))


#3
# def d(n):
#     lst = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(201455, 201471):
#     n = d(i)
#     if len(n) == 4:
#         print(n)


#4 ?????
for i in range(2000000, 3000001):
    sqrti = i**0.5 
    k = 0
    for j in range(1, round(sqrti)):
        if i % j == 0:
            if (abs(i / j) - j) <= 115:
                k += 1
    if k > 2: print(i)
    k = 0


#1 pro
# def d(n):
#     lst = []
#     for i in range(1, int(n ** 0.5) +1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# def N(k):
#     return 750000 + k

# c1 = 0
# for k in range(1, 6):
#     a = d(N(k))
#     for i in a:
#         if i % 2 == 0:
#             c1 += 1
#             if c1 % 2 != 0:
#                 print(k, c1)
    
            
#2
# def d(n):
#     lst = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             global l
#             l = n // i
#             m = l - i
#             if m <= 90:
#                 lst.append(m)
#     return sorted(set(lst))

# for i in range(500000, 1000001):
#     n = d(i)
#     if len(n) >= 3:
#         print(i, l)