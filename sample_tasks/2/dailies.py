#1  xwzy
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = x and (z <= w) and (not y)
#                 if f == 1:
#                     print(x, y, z, w)


#2  yxwz
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (not(((not x) or y) and (not w))) or (not (z and (not (y and w))))
#                 if f == 0:
#                     print(x, y, z, w)


#3  zwxy
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x <= (y <= z)) and (y <= (z == (not w)))
#                 if f == 0:
#                     print(x, y, z, w)


#4  xzyw
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (y <= (not (x <= z))) or w
#                 if f == 0:
#                     print(x, y, z, w)


#5  yxwz
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (not(x <= w)) or (y <= z) or (not y)
#                 if f == 0:
#                     print(x, y, z, w)


#6  dcba
# print("a b c d")
# for a in 0, 1:
#     for b in 0, 1:
#         for c in 0, 1:
#             for d in 0, 1:
#                 f = (a <= b) and (b <= (not c)) and ((not c) <= d)
#                 if f == 1:
#                     print(a, b, c, d)


#7
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x <= (z == w)) or (not(y <= w))
#                 if f == 0:
#                     print(x, y, z, w)


#8
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x <= y) and ((not y) == z) and w
#                 if f == 1:
#                     print(x, y, z, w)


#9
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(x, y, z, w)


#10
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x <= y) or (z == x)) and (w <= z)
#                 if f == 0:
#                     print(x, y, z, w)