#1      base
# print("x y z")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             f = (x or y) <= (z == x)
#             if f == 0:
#                 print(x, y, z)


#2
# print("x y z")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             f = (x == z) or (x <= (y and z))
#             if f == 0:
#                 print(x, y, z)


#3
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= y) and (y <= w)) or (z == (x or y))
#                 if f == 0:
#                     print(x, y, z, w)


#4
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x == (w or y)) or ((w <= z) and (y <= w))
#                 if f == 0:
#                     print(x, y, z, w)


#5
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= y) == (z <= w)) or (x and w)
#                 if f == 0:
#                     print(x, y, z, w)


#1      pro
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x and y) or (y and z)) == ((x <= w) and (w <= z))
#                 if f == 1:
#                     print(x, y, z, w)


#2
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x and w) or (w and z)) == ((z <= y) and (y <= x))
#                 if f == 1:
#                     print(x, y, z, w)


#3
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (y == z) or ( not w)
#                 if f == 0:
#                     print(x, y, z, w)


#4
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(x, y, z, w)


#5
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (y == z) or (not w)
#                 if f == 0:
#                     print(x, y, z, w)