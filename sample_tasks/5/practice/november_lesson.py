#1
# for i in range(1, 100):
#     n = bin(i)[2:]

#     n = n + str(n.count("1") % 2) #более короткий способ, чем в теории
#     n = n + str(n.count("1") % 2)

#     r = int(n, 2) #перевод в 10чную систему
#     if r > 77:
#         print(i)
#         break


#2 
# for i in range(1, 9):
#     n = bin(i)[2:]
#     if i % 2 == 0:
#         n = "10" + n
#     else:
#         n = "1" + n + "01"
#     r = int(n, 2)
#     print(r)


#3
# for i in range(1, 100):
#     N = i
#     n = bin(N)[2:]
#     if n.count("1") % 2 == 0:
#         n = "10" + n[2:] + "0"
#     else:
#         n = "11" + n[2:] + "1"
#     r = int(n, 2)
#     if r >= 16:
#         print(i)
#         break


#4
# for i in range(1, 100):
#     N = i
#     n = bin(N)[2:]
#     if N % 2 != 0:
#         n += "0"
#     else:
#         n = "1" + n
#     if n.count("1") % 2 == 0:
#         n += "1"
#     else:
#         n += "0"
#     r = int(n, 2)
#     if r > 228:
#         print(i)
#         break


#5!(чуть сложнее. перевод в троичную сс)
# def convert(n, base):
#     s = ""
#     while n > 0:
#         s = str(n % base) + s
#         n = n // base
#     return s

# lst = []
# for i in range(1, 1000000):
#     N = i
#     n = convert(N, 3)
#     if N % 3 == 0:
#         n += n[-2:]
#     else:
#         n = n + convert(N % 3 * 5, 3) 

#     r = int(n, 3)
#     if r > 133:
#         lst.append(r)
# print(min(lst))


#7
# for j in range(128, 256):
#     N = j
#     n = bin(N)[2:].zfill(8) #!!!
#     n1 = ""
#     for i in n:
#         if i == "1":
#             n1 += "0"
#         else:
#             n1 += "1"

#     r = N - int(n1, 2)
#     if r == 105:
#         print(j)
    
