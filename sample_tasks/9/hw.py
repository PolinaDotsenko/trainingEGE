#1
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\09.txt"):
#     a = [int(x) for x in i.split()]
#     a.sort()
#     if a[0]**2 + a[1]**2 == a[2]**2:
#         c += 1
# print(c)


#2
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9.txt"):
#     a = [int(x) for x in i.split()]
#     pov = [x for x in a if a.count(x) == 2]
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(set(pov)) == 2 and len(nepov) == 3 and sum(nepov) / len(nepov) > sum(pov) / len(pov):
#         c += 1
# print(c)


#3
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-248.txt"):
#     a = [int(x) for x in i.split()]
#     pov = [x for x in a if a.count(x) == 3]
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(pov) == 3 and len(nepov) == 3 and \
#         sum(pov)**2 > sum(nepov)**2:
#             c += 1
# print(c)


#4
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-58322.txt"):
#     a = [int(x) for x in i.split()]
#     a.sort()
#     if a[-1]**2 > (a[0] * a[1] * a[2]) or \
#         a[1] - a[0] == a[2] - a[1] == a[3] - a[2]: 
#         c += 1
# print(c)


#5
# c = 0 
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-249.txt"):
#     a = [int(x) for x in i.split()]
#     po = [x for x in a if a.count(x) >= 3]
#     pov = [x for x in a if a.count(x) > 1]
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(po) >= 3 and len(nepov) > 0 and \
#         sum(pov) / len(pov) > sum(nepov) / len(nepov):
#             c += 1
# print(c)


#6
# c = 0 
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-245.txt"):
#     a = [int(x) for x in i.split()]
#     pov = [x for x in a if a.count(x) == 3]
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(pov) == 3 and len(nepov) == 3 and \
#         sum(pov)**2 > sum(nepov)** 2:
#         c += 1
# print(c)


#7
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-244.txt"):
#     a = [int(x) for x in i.split()]
#     a.sort()
#     t = [x for x in a if a.count(x) == 2]
#     if a[-1] < sum(a[:3]) and len(t) == 2:
#         c += 1
# print(c)


#8
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-228.txt"):
#     a = [int(x) for x in i.split()]
#     a.sort()
#     pov = [x for x in a if a.count(x) == 2]
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(pov) == 4 and (a[0] + a[-1]) / 2 < sum(a[1:5]) / 4:
#         c += 1
# print(c)


#9
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-228-(1).txt"):
#     a = [int(x) for x in i.split()]
#     a.sort()
#     pov = [x for x in a if a.count(x) == 2]
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(pov) == 2 and len(nepov) == 4 and \
#         (a[0] + a[-1]) / 2 > sum(a[1:5]) / 4:
#         c += 1
# print(c)


#10
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-228-(2).txt"):
#     a = [int(x) for x in i.split()]
#     a.sort()
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(nepov) == 6 and (a[0] + a[-1]) / 2 > sum(a[1:5]) / 4:
#         c += 1
# print(c)