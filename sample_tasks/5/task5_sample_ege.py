#универсальный алгоритм для перевода сс
# def convert(n, base):
#     s = ""
#     while n > 0:
#         s = str(n % base) + s
#         n = n // base
#     return s



#1 тип 5 задания (перевод в другие системы)

# N = int(input())
# n = bin(N)[2:] #отрубает 2 знака сначала 
# if n.count("1") % 2 != 0: 
#     n = n + "1"
# else:
#     n = n + "0"
# if n.count("1") % 2 != 0:
#     n = n + "1"
# else:
#     n = n + "0"
# r = int(n, 2) #перевод в 10чную систему

# print(r)


#2 тип задания (посимвольное десятичное преобразование)

for i in range(100, 1000): #проходимся по трехзначным числам
    N = i
    n1 = int(str(N)[0]) #выделяем цифры из числа
    n2 = int(str(N)[1])
    n3 = int(str(N)[2])

    s1 = n1 + n2 
    s2 = n2 + n3

    ans = str(max(s1, s2)) + str(min(s1, s2)) #записываем в порядке убывания
    if ans == "1412":
        print(i)