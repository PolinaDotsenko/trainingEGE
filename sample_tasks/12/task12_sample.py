#Исполнитель Редактор задание
#1
# s = 146 * "5"
# while "333" in s or "555" in s:
#     if "555" in s:
#         s = s.replace("555", "3", 1)
#     else:
#         s = s.replace("333", "5", 1)
# print(s)


#2
# s = "1" + 80 * "8"
# while "18" in s or "288" in s or "3888" in s:
#     if "18" in s:
#         s = s.replace("18", "2", 1)
#     elif "288" in s:
#         s = s.replace("288", "3", 1)
#     else:
#         s = s.replace("3888", "1", 1)
# print(s)


#3
# s = 99 * "8" + "1"
# while "133" in s or "881" in s:
#     if "133" in s:
#         s = s.replace("133", "81", 1)
#     else: 
#         s = s.replace("881", "13", 1)
# print(s)


#4
# for i in range(201, 215):
#     s = i * "1"
#     while "1111" in s:
#         s = s.replace("1111", "22", 1)
#         s = s.replace("222", "1", 1)
#     print(s, i)


#5
# for n in range(1, 10000):
#     s = ">" + 39 * "0" + n * "1" + 39 * "2"
#     while ">1" in s or ">2" in s or ">0" in s:
#         if ">1" in s:
#             s = s.replace(">1", "22>", 1)
#         if ">2" in s:
#             s = s.replace(">2", "2>", 1)
#         if ">0" in s:
#             s = s.replace(">0", "1>", 1)
#     su = 2 * s.count("2") + s.count("1")
#     if su % 3837 == 0:
#         print(n)


#6
# for one in range(1, 50):
#     for two in range(1, 50):
#         for three in range(1, 50):
#             s = "0" + one * "1" + two * "2" +  three * "3" + "0"
#             while "00" not in s:
#                 s = s.replace("01", "210", 1)
#                 s = s.replace("02", "3101", 1)
#                 s = s.replace("03", "2012", 1)
#             if s.count("1") == 61 and s.count("2") == 50 and s.count("3") == 18:
#                 print(one + two + three + 2)


#8
# c = 0
# s = 500 * "5"
# while "555" in s or "333" in s:
#     if "333" in s:
#         s = s.replace("333", "5", 1)
#         c += 3
#     else:
#         s = s.replace("555", "3", 1)
# print(c)