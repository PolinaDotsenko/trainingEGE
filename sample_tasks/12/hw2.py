#1
# s = "2" + "5" * 81
# while "25" in s or "355" in s or "4555" in s:
#     if "25" in s:
#         s = s.replace("25", "4", 1)
#     if "355" in s:
#         s = s.replace("355", "2", 1)
#     if "4555" in s:
#         s = s.replace("4555", "3", 1)
# print(s)


#2
# s = "4" + "5" * 90
# while "25" in s or "355" in s or "4555" in s:
#     if "25" in s:
#         s = s.replace("25", "3", 1)
#     if "355" in s:
#         s = s.replace("355", "4", 1)
#     if "4555" in s:
#         s = s.replace("4555", "2", 1)
# print(s)


#3
# s = "3" + "5" * 57
# while "25" in s or "355" in s or "4555" in s:
#     if "25" in s:
#         s = s.replace("25", "3", 1)
#     if "355" in s:
#         s = s.replace("355", "4", 1)
#     if "4555" in s:
#         s = s.replace("4555", "2", 1)
# print(s)


#4
# s = "3" * 207
# while "9999" in s or "333" in s:
#     if "9999" in s:
#         s = s.replace("9999", "3", 1)
#     else:
#         s = s.replace("333", "99", 1)
# print(s)


#5
# s = "9" * 207
# while "9999" in s or "333" in s:
#     if "9999" in s:
#         s = s.replace("9999", "3", 1)
#     else:
#         s = s.replace("333", "99", 1)
# print(s)


#6
# s = "3" * 194
# while "9999" in s or "333" in s:
#     if "9999" in s:
#         s = s.replace("9999", "3", 1)
#     else:
#         s = s.replace("333", "99", 1)
# print(s)


#7
# lst = []
# for n in range(4, 1000):
#     s = "1" + "2" * n
#     while "12" in s or "322" in s or "222" in s:
#         if "12" in s:
#             s = s.replace("12", "2", 1)
#         if "322" in s:
#             s = s.replace("322", "21", 1)
#         if "222" in s:
#             s = s.replace("222", "3", 1)
#     lst.append(s)
# print(len(max(lst, key=len)))