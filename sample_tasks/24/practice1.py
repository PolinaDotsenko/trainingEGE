#простой пример
# f = open("sample_tasks\\24\\files\\k7a-4.txt").readline()

# m = 0
# for l in range(len(f)):
#     for r in range(l + m, len(f)):
#         s = f[l:r+1]
#         if "D" not in s:
#             m = max(m, len(s))
#         else:
#             break
# print(m)


#1
# f = open("sample_tasks\\24\\files\\1.txt").readline()
# for i in range(1, 100):
#     if i * "Z" in f:
#         print(i)


#2
# f = open("sample_tasks\\24\\files\\24-264.txt").readline()

# for i in "QWERTYUIOPASDFGHJKLZXCVBNM":
#     f = f.replace(i, "a")
# for i in "0123456789":
#     f = f.replace(i, "0")

# m = 0
# for l in range(len(f)):
#     for r in range(l + m, len(f)):
#         s = f[l:r+1]
#         if "aa" not in s and "00" not in s:
#             m = max(0, len(s))
#         else:
#             break
# print(m)


#3      s[0] != 0
# f = open("sample_tasks\\24\\files\\24-264.txt").readline()

# for i in "QWRTYUIOPSGHJKLZXVNM":
#     f = f.replace(i, " ")

# m = 0
# for l in range(len(f)):
#     for r in range(l + m, len(f)):
#         s = f[l:r+1]
#         if s[0] != 0:
#             if " " not in s:
#                 m = max(m, len(s))
#             else:
#                 break
# print(m)


#4  четность определяется по последней цифре. работает только с сс с четным основанием
# f = open("sample_tasks\\24\\files\\24-334.txt").readline()

# for i in "QWERTYUIOPSDFGHJKLZXCVNM":
#     f = f.replace(i, "z")

# m = 0
# for l in range(len(f)):
#     for r in range(l + m, len(f)):
#         s = f[l:r+1]
#         if s[0] != 0 and "z" not in s:
#             if s[-1] in "02468A":
#                 m = max(m, len(s))
#         else:
#             break
# print(m)


#5
# f = open("sample_tasks\\24\\files\\24-181.txt").readline()

# m = 0
# for l in range(len(f)):
#     for r in range(l + m, len(f)):
#         s = f[l:r+1]
#         if s.count(".") <= 2:
#             m = max(m, len(s))
#         else:
#             break
# print(m)


#6
# f = open("sample_tasks\\24\\files\\24-263.txt").readline()

# m = 0
# for l in range(len(f)):
#     for r in range(l + m, len(f)):
#         s = f[l:r+1]
#         if s.count("Y") <= 150:
#             m = max(m, len(s))
#         else:
#             break
# print(m)


#6 !!!!!MIN
# f = open("sample_tasks\\24\\files\\24-263.txt").readline()

# m = 10000
# for l in range(len(f)):
#     for r in range(l + m, l, -1):
#         s = f[l:r+1]
#         if s.count("Z") >= 120:
#             m = min(m, len(s))
#         else:
#             break
# print(m)


#7  !!!
# f = open("sample_tasks\\24\\files\\24-224.txt").readline()

# f = f.replace("CAB", "*")
# f = f.replace("BAC", "*")

# for i in range(1, 100):
#     if i * "*" in f:
#         print(i * 3)  #кол-во символов


#8  !!!
# f = open("sample_tasks\\24\\files\\8.txt").readline()

# f = f.replace("C", "F")
# f = f.replace("D", "F")
# f = f.replace("O", "A")

# f = f.replace("FFA", "*")

# for i in range(1, 100):
#     if i * "*" in f:
#         print(i)  #кол-во групп символов