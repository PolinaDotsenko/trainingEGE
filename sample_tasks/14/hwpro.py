#1
# n = 9**81 + 27**729 - 4
# lst = []
# while n > 0:
#     lst.append(n % 9)
#     n = n // 9
# s = [max(lst) if i == 0 else i for i in lst]
# print(s.count(max(s)))


#2
# n =  12 * 7**135 + 11 * 7**92 - 63 * 7**22 + 17 * 7**11 + 157
# lst = []
# while n > 0:
#     lst.append(n % 7)
#     n = n // 7
# print(len(set(lst)))


#3
# n = 5 * 216**1256 - 5 * 36**1146 + 4 * 6**1053 - 1087
# lst = []
# while n > 0:
#     lst.append(n % 6)
#     n = n // 6
# print(sum(lst))


#4
# for x in range(0, 22):
#     a = f"7{x}38596"
#     b = f"14{x}36"
#     c = f"61{x}7"
#     res = int(a, 23) + int(b, 23) + int(c, 23)
#     if res % 22 == 0:
#         print(res / 22)

