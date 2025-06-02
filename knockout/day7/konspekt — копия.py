1

for n in range(6, 36):
    if (7**500 - int('53', n)) % 6 == 0:
        print(n)


2

for x in range(0, 36):
    a = 5 + 4*36 + x*36**2 + 2*36**3 + 1*36**4
    b = x + 12345
    if (a + b) % 13 == 0:
        print(x, (a + b) // 13)


3

for x in range(11):
    for y in range(11):
        a = 5 + x*25 + 3*25**2 + 2*25**3 + y*25**4 + 7*25**5
        b = y + 9*11**1 + x*11**2 + 7*11**3 + 6*11**4
        if (a + b) % 131 == 0:
            print(x, y, (a + b) // 131)


4

for x in range(1, 22):
    for y in range(13):
        a = 5 + x*22 + 3*22**2 + 2*22**3 + x*22**4
        b = y + 9*13 + y*13**2 + 7*13**3 + 6*13**4
        if (a - b) % 57 == 0:
            print(x, y, (a - b) // 57)


6

def f(n, base):
    lst = []
    while n > 0:
        lst.append(n % base)
        n = n // base
    return lst[::-1]

for x in range(1, 1000):
    n = 5**2026 + 7*5**1013 + 107 - x
    s = f(n, 6)
    if s.count(5) - s.count(0) == 28:
        print(x)
        break


7

n = 8**888 + 15*15**1515 - 2**444
s = oct(n)[2:]
print(s.count('71') + s.count('72') + s.count('73') + s.count('74') + s.count('75') + s.count('76'))


8

def f(n, base):
    lst = []
    while n > 0:
        lst.append(n % base)
        n = n // base
    return lst[::-1]

n = (5**300 * 15**100) - (25**50 + 125**100)
s = f(n, 5)
print(sum(s) - s.count(4)*4)



10

f = open('26-k1.txt')
n, k = map(int, f.readline().split())
lst = sorted([int(x) for x in f])[::-1]
skidki = sum(lst[:k]) * 0.2
print(lst[k], skidki)


10(2)

f = open('26-k1.txt')
n, k = map(int, f.readline().split())
lst = [int(x) for x in f]
lst.sort(reverse=True)
skidki = sum(lst[:k]) * 0.2
print(lst[k], skidki)


11

f = open('26-k2.txt')
n, k = map(int, f.readline().split())
lst = sorted([int(x) for x in f])
lst = lst[k:-k]
print(max(lst), sum(lst)/len(lst))


12

f = open('26-k3.txt')
n, k, m = map(int, f.readline().split())
lst = sorted([int(x) for x in f])[::-1]
pob = lst[:k]
priz = lst[k:k+m]
print(min(priz), min(pob))



14

f = open('26-111.txt')
k = int(f.readline())
n = int(f.readline())
time = []
for i in f:
    a, b = map(int, i.split())
    time.append([a, b])
time.sort()
a = k * [0]
c = 0
last = 0
for i in range(len(time)):
    for j in range(len(a)):
        if time[i][0] > a[j]:
            a[j] = time[i][1]
            c += 1
            last = j + 1
            break
print(c, last)



15

f = open('26-89.txt')
n = int(f.readline())
lst = [int(x) for x in f]
lst.sort(reverse=True)
a = [lst[0]]
for i in range(1, len(lst)):
    if a[-1] - lst[i] >= 3:
        a.append(lst[i])
print(len(a), a[-1])

