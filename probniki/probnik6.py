#2
# print("x y z w")
# for x in 0, 1:
#     for y in 0, 1:
#         for z in 0, 1:
#             for w in 0, 1:
#                 f = (x and (not y)) or (x == z) or w
#                 if f == 0:
#                     print(x, y, z, w)


#16
# def f(n):
#     if n >= 1300: return n
#     if n < 1300 and n % 2 != 0: return n * f(n + 1)
#     if n < 1300 and n % 2 == 0: return (n * f(n + 2)) / 4
# print(f(1286) / f(1290))