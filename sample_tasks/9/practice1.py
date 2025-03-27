#1
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-246.txt"):
#     a = [int(x) for x in i.split()] #!!!
#     a.sort()
#     if a[3] + a[0] <= a[1] + a[2]:
#         c += 1
# print(c)


#3
# c = 0 
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-162.txt"):
#     a = [int(x) for x in i.split()]
#     a.sort()
#     if a[3] - a[0] >= 50 and a[1] * a[2] <= 1000:
#         c += 1
# print(c)


#4
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-253.txt"):
#     a = [int(x) for x in i.split()]
#     pov = [x for x in a if a.count(x) == 3]
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(set(pov)) == 2 and sum(pov) / len(pov) < nepov[0]:
#         c += 1
# print(c)


#5
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-248.txt"):
#     a = [int(x) for x in i.split()]
#     pov = [x for x in a if a.count(x) == 3]
#     nepov = [x for x in a if a.count(x) == 1]
#     if len(nepov) == 3 and sum(pov)**2 > sum(nepov)**2:
#         c += 1
# print(c)


#6
# c = 0
# for i in open("trainingEGE\\sample_tasks\\9\\files\\9-247.txt"):
#     a = [int(x) for x in i.split()]
#     a.sort()
#     if len(set(a)) == 4 and a[3] + a[0] > a[1] + a[2]:
#         c += 1
# print(c)