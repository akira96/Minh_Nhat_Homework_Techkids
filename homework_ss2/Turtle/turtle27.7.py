from turtle import *

##Setting
speed(-1)
color("red")

##Draw
#1
rt(60)
for i in range (4):
    for i in range (2):
        fd(50)
        rt(60)
        fd(50)
        rt(120)
    lt(90)
    
##------------------------
color("white")
lt(60)
fd(150)
##------------------------
#2
for n in range (3,7):
    for i in range(n):
        if n%2:
            color("red")
        else:
            color("blue")
        fd(100)
        lt(360/n)
