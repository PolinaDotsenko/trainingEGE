#6
from turtle import *

screensize(100000, 100000)
tracer(0)
k = 25

lt(90)
down()
for i in range(9):
    fd(12 * k)
    rt(90)
    fd(6 * k)
    rt(90)
up()
fd(k)
rt(90)
fd(3 * k)
lt(90)    
down()
for i in range(9):
    fd(53 * k)
    rt(90)
    fd(75 * k)
    rt(90)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(3, "pink")
exitonclick()