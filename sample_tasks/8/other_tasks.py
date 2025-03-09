#1
from itertools import *

lst = []
for i in product(range(12), repeat=5):
    if i.count(7) == 1 and sorted(i)[-4] < 9:
        lst.append(i)
print(len(lst))