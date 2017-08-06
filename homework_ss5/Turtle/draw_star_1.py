from turtle import *
x = int(input("x:"))
y = int(input("y:"))
length = int(input("length:"))
color('red')
speed(-1)
#draw
def draw_star(x, y, length):
     penup()
     fd(x)
     lt(90)
     fd(y)
     rt(90)
     pendown()
     lt(36)
     for i in range(5):
          fd(length)
          lt(144)
         
draw_star(x, y, length)
