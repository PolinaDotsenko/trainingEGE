#1
# f = open("sample_tasks\\24\\files\\24.txt")
# lst = [x[:-1] for x in f]

# g = 1000
# for i in lst:
#     if i.count("G") < g:
#         g = min(g, i.count("G"))
#         s = i

# a = []
# res = []
# for i in "QWERTYUIOPASDFGHJKLZXCVBNM":
#     if i in s:
#         a.append(s.count(i))
#     if max(a) == s.count(i):
#         res.append(i)
# print(sorted(res)[-1])


#2
# f = open("sample_tasks\\24\\files\\24 (1).txt").readline()

# f = f.replace("C", "F")
# f = f.replace("D", "F")
# f = f.replace("O", "A")

# f = f.replace("FA", "*")

# for i in range(1, 300):
#     if i * "*" in f:
#         print(i)


#3
f = open("sample_tasks\\24\\files\\1_24.txt").readline()

m = 10**10
c = 0
pos = []
for i in range(len(f) - 1):
    if f[i] + f[i + 1] == "TT":
        pos.append(i)
        for j in range(0, len(pos) - 149):
            c = pos[j + 149] - pos[j] + 2
            if c < m:
                m = c
print(m)


#4
# f = open("sample_tasks\\24\\files\\24-(3).txt").readline()

# m = 10000
# for l in range(len(f)):
#     for r in range(l + m, l, -1):
#         s = f[l:r+1]
#         if s.count("W") >= 130:
#             m = min(m, len(s))
#         else:
#             break
# print(m)


#5
# f = open("sample_tasks\\24\\files\\24-(4).txt").readline()

# m = 10000
# for l in range(len(f)):
#     for r in range(l + m, l, -1):
#         s = f[l:r+1]
#         if s.count("V") >= 120:
#             m = min(m, len(s))
#         else:
#             break
# print(m)