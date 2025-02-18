#1
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
# print("x y z")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             f = (x == y) or ((y or z) <= x)
#             if f == 0:
#                 print(x, y, z)


#4
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= y) and (y <= w)) or (z == (x or y))
#                 if f == 0:
#                     print(x, y, z, w)


#5
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (z and y) or ((x <= z) == (y <= w))
#                 if f == 0:
#                     print(x, y, z, w)


#6
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= z) <= y) or (not w)
#                 if f == 0:
#                     print(x, y, z, w)


#7
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (not (w <= z)) or (x <= y) or (not x)
#                 if f == 0:
#                     print(x, y, z, w)


#8
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (not (x <= z)) or (y == w) or y
#                 if f == 0:
#                     print(x, y, z, w)


#9
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x)))
#                 if f == 0:
#                     print(x, y, z, w)