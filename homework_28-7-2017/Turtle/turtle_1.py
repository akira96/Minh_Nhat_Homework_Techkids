from turtle import *

speed(-1)
colors = ['red', 'blue', 'brown', 'yellow', 'grey']
n = 3

for a in range(n, n + len(colors)):
        color(colors[a-3])
        for i in range(n):
                fd(100)
                lt(360/n)
        n += 1
        
input()
