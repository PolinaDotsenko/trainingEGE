#1
# from turtle import *
# screensize(100000, 100000)
# tracer(0)
# k = 35

# lt(90)
# down()
# for i in range(12):
#     rt(60)
#     fd(k)
#     rt(60)
#     fd(k)
#     rt(270)
# up()

# for x in range(-100, 100):
#     for y in range(-100, 100):
#         goto(x * k, y * k)
#         dot(5, "red")
# exitonclick()


#2
# from turtle import *
# screensize(100000, 100000)
# tracer(0)
# k = 40

# lt(90)
# down()
# for i in range(4):
#     fd(7 * k)
#     rt(90)
#     fd(8 * k)
#     rt(90)
# up()

# for x in range(-50, 50):
#     for y in range(-50, 50):
#         goto(x * k, y * k)
#         dot(5, "pink")
# exitonclick()


#3
from turtle import *
screensize(100000, 100000)
tracer(0)
k = 50

lt(90)
down()
for i in range(4):
    fd(14 * k)
    rt(90)
for i in range(5):
    fd(5 * k)
    rt(45)
up()

for x in range(-50, 50):
    for y in range(-50, 50):
        goto(x * k, y * k)
        dot(5, "red")
exitonclick()