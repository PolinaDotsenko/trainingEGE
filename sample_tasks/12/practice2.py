#1
# s = "5" * 146
# while "333" in s or "555" in s:
#     if "555" in s:
#         s = s.replace("555", "3", 1)
#     else: 
#         s = s.replace("333", "5", 1)
# print(s)


#2
# s = "1" + ("8" * 80)
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
# for i in range(201, 210):
#     s = "1" * i
#     while "1111" in s:
#         s = s.replace("1111", "22", 1)
#         s = s.replace("222", "1", 1)
#     if s.count("1") == 0:
#         print(i)


#!!!5
# for i in range(1, 1000):
#     s = ">" + 39 * "0" + i * "1" + 39 * "2"
#     while ">1" in s or ">2" in s or ">0" in s:
#         if ">1" in s:
#             s = s.replace(">1", "22>", 1)
#         if ">2" in s:
#             s = s.replace(">2", "2>", 1)
#         if ">0" in s:
#             s = s.replace(">0", "1>", 1)
#     res = s.count("1") + s.count("2") * 2
#     if res % 3837 == 0:
#         print(i)
#         break


#6
# for one in range(1, 50):
#     for two in range(1, 50):
#         for three in range(1, 50):
#             s = "0" + one * "1" + two * "2" + three * "3" + "0"
#             while "00" not in s:
#                 s = s.replace("01", "210", 1)
#                 s = s.replace("02", "3101", 1)
#                 s = s.replace("03", "2012", 1)
#             if s.count("1") == 61 and s.count("2") == 50 and s.count("3") == 18:
#                 print(one + two + three + 2)    #!не забыть про нули (2)


#7
# s = 50 * "1" + 50 * "2" + 50 * "3"
# while "21" in s or "31" in s or "23" in s:
#     if "21"in s:
#         s = s.replace("21", "12", 1)
#     if "31"in s:
#         s = s.replace("31", "13", 1)
#     if "23"in s:
#         s = s.replace("23", "32", 1)
# print(s[9], s[89], s[129])