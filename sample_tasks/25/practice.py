#теория
#1
# for i in range(0, 10):
#     for j in range(0, 10):
#         n = int("12345" + str(i) + "7" + str(j) + "8")
#         if n % 23 == 0:
#             print(n, n // 23)


#2!
# def f(n):
#     lst = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# print(f(1000000000000))


#практика 1
#1
# def d(n):
#     lst = []
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(174457, 174506):
#     n = d(i)
#     if n == 2:
#         print(n)


#2
# def d(n):
#     lst = []
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(210235, 210301):
#     n = d(i)
#     if len(n) == 4:
#         print(n)


#3
# def d(n):
#     lst = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(312614, 312652):
#     n = d(i)
#     if len(n) == 6:
#         print(n)


#4
# def d(n):
#     lst = []
#     for i in range(1, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(110203, 110246):
#     n = d(i)
#     chet = [x for x in n if x % 2 == 0]
#     if len(chet) == 4:
#         print(chet)


#5
# def d(n):
#     lst = []
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# count = 0
# for i in range(452022, 10000000):
#     if count == 5:
#         break
#     n = d(i)
#     if len(n) > 0:
#         m = max(n) + min(n)
#         if m % 7 == 3:
#             print(i, m)
#             count += 1

