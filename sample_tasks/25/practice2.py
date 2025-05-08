#1
# def f(n):
#     lst = []
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(174457, 174506):
#     if len(f(i)) == 2:
#         print(f(i))


#2
# def f(n):
#     lst = []
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(210235, 210301):
#     if len(f(i)) == 4:
#         print(f(i))


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


#4 маска и делители
# from fnmatch import *

# def f(n):
#     for i in range(2, int(n**0.5) + 1):
#         if n % i == 0:
#             return False
#     return True
            
# for i in range(2627, 10**9, 2627):
#     if fnmatch(str(i), "7*53?3*1"):
#         su = sum(int(x) for x in str(i))
#         if f(su):
#             print(i, i // 2627)
            
            
#5
# def f(n):
#     lst = []
#     for i in range(1, int(n**0.5) + 1):
#         if n % i == 0:
#             lst.append(i)
#             lst.append(n // i)
#     return sorted(set(lst))

# for i in range(110203, 110246):
#     a = [x for x in f(i) if x % 2 == 0]
#     if len(a) == 4:
#         print(a)
        
        
#6 было в демо
def f(n):
    lst = []
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            lst.append(i)
            lst.append(n // i)
    return sorted(set(lst))

c = 0
for i in range(452022, 452122):
    a = f(i)
    if len(f(i)) != 0:
        m = max(a) + min(a)
        if m % 7 == 3:
            print(i, m)
            c += 1
        if c == 5:
            break