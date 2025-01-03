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
# l = 0
# def d(n):
#     lst = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append((n // i) - i)
#     return sorted(set(lst))

# c = 0
# for i in range(2000000, 3000000):
#     n = d(i)
#     for x in n:
#         if x <= 115:
#             c += 1
#     if c >= 3:
#         print(n)


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
def d(n):
    lst = []
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            global l
            l = n // i
            m = l - i
            if m <= 90:
                lst.append(m)
    return sorted(set(lst))

for i in range(500000, 1000001):
    n = d(i)
    if len(n) >= 3:
        print(i, l)