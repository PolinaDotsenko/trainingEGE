#1
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x)))
#                 if f == 0:
#                     print(x, y, z, w)


#2
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((z <= y) and ((not x) <= w)) <= ((z == w) or (y and (not x)))
#                 if f == 0:
#                     print(x, y, z, w)
                    

#3
# print("a b c d")
# for a in 0, 1:
#     for b in 0, 1:
#         for c in 0, 1:
#             for d in 0, 1:
#                 f = ((a and b) == (not c)) and (b <= d)
#                 if f == 1:
#                     print(a, b, c, d)


#4
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((not x) == z) <= (y == (w or x))
#                 if f == 0:
#                     print(x, y, z, w)


#5
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x and w) or (w and z)) == ((z <= y) and (y <= x))
#                 if f == 1:
#                     print(x, y, z, w)


#6
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((x and (not y)) or (w <= z)) == (z == x)
#                 if f == 1:
#                     print(x, y, z, w)


#7
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (y == z) or w
#                 if f == 0:
#                     print(x, y, z, w)


#8
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x == (not y)) <= ((z <= (not w)) and (w <= y))
#                 if f == 0:    #меняю значение
#                     print(x, y, z, w)
