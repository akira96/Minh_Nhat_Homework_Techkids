from turtle import *
x = int(input("x:"))
y = int(input("y:"))
length = int(input("length:"))


#draw
def draw_star(x, y, length):
     penup()
     forward(x)
     left(90)
     forward(y)
     right(90)
     pendown()
     left(36)
     for i in range(5):
          forward(length)
          left(144)
speed(0)
color('blue')
for i in range(100):
    import random
    x = random.randint(-300, 300)
    y = random.randint(-300, 300)
    length = random.randint(3, 10)
    draw_star(x, y, length)
    
# Ham random.randint se cho gia tri ngau nhien cho x & y trong khoang (-300,300)
                                             # va cho length trong khoang(3, 10)

