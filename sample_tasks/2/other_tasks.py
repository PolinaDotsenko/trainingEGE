#пример аналитического кода 
# print("x y w z")
# for x in 0, 1:
#     for y in 0, 1:
#         for w in 0, 1:
#             for z in 0, 1:
#                 f = (x and (not y)) or (y == z) or w
#                 if f == 0:
#                     print(x, y, w, z)


#1
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = ((w <= y) <= x) or (not z)
#                 if f == 0:
#                     print(x, y, z, w)


#2
print("x y z w")
for x in 0, 1:
    for y in 0, 1:
        for z in 0, 1:
            for w in 0, 1:
                f = (w or x or y) <= ((y or z) and x or y and (w or z))
                if f == 0:
                    print(x, y, z, w)