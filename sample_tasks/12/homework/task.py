#1
# s = 1000 * "9"
# while "999" in s or "888" in s:
#     if "888" in s:
#         s = s.replace("888", "9", 1)
#     else:
#         s = s.replace("999", "8", 1)
# print(s)


#2
# s = 1000 * "8"
# while "999" in s or "888" in s:
#     if "888" in s:
#         s = s.replace("888", "9", 1)
#     else:
#         s = s.replace("999", "8", 1)
# print(s)


#3
# s = ">" + 10 * "1" + 20 * "2" + 30 * "3"
# while ">1" in s or ">2" in s or ">3" in s :
#     if ">1" in s:
#         s = s.replace(">1", "22>", 1)
#     if ">2" in s:
#         s = s.replace(">2", "2>", 1)
#     if ">3" in s:
#         s = s.replace(">3", "1>", 1)
# print(s.count("1") + 2 * s.count("2") + 3 * s.count("3"))


#4
# for one in range(0, 65):
#     for two in range(0, 65):
#         for three in  range(0, 65):
#             s = "0" + "1" * one + "2" * two + "3" * three
#             while "01" in s or "02" in s or "03" in s:
#                 s = s.replace("01", "30", 1)
#                 s = s.replace("02", "101", 1)
#                 s = s.replace("03", "202", 1)
#             if s.count("1") == 15 and s.count("2") == 10 and s.count("3") == 60:
#                 print(one)


#5
# s = "1" + 98 * "9"
# while "19" in s or "299" in s or "3999" in s:
#     s = s.replace("19", "2", 1)
#     s = s.replace("299", "3", 1)
#     s = s.replace("3999", "1", 1)
# print(s)


#6
# s = 82 * "8"
# while "1111" in s or "8888" in s:
#     if "1111" in s:
#         s = s.replace("1111", "8", 1)
#     else:
#         s = s.replace("8888", "11", 1)
# print(s)


#7
# s = 108 * "7"
# while "33333" in s or "777" in s:
#     if "33333" in s:
#         s = s.replace("33333", "7", 1)
#     else:
#         s = s.replace("777", "3", 1)
# print(s)

#все правильно