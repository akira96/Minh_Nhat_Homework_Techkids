from turtle import *
length = int(input("length:"))
square_color = input("color:")
speed(-1)
#draw
def draw_square(length, square_color):
     color(str(square_color))
     for i in range(4):
          fd(length)
          lt(90)
          
for i in range(30):
    draw_square(i * 5, 'red')
    left(17)
    penup()
    forward(i * 2)
    pendown()

input()
