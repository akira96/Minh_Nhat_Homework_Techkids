from turtle import *

speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']

for i in range(5):
        color(colors[i])
        begin_fill()
        for j in range(4):
                if (j%2) == 1:
                        fd(100)
                else:
                        fd(50)
                lt(360/4)
        end_fill()
        fd(50)
input()
