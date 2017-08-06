#Map
px = 2
py = 1
bx = 1
by = 2
gx = 1
gy = 3
x = 0
y = 0

def map_game(x, y, px, py, gx, gy, bx, by):
     for y in range(4):
          for x in range(4):
               if x == px and y == py:
                    print("P", end = " ")
               elif x == gx and y == gy:
                    print("G", end = " ")
               elif x == bx and y == by:
                    print("B", end = " ")
               else:
                    print("-", end = " ")
          print()
map_game(x, y, px, py, gx, gy, bx, by)

#Move
while (bx != gx or by != gy):
     command = str(input("Your move?"))
     if command.upper() == "D":
          if px == 3:
               print("Cannot go right!")
          elif py == by and px + 1 == bx:
               px += 1
               bx += 1
          else:
               px += 1
     elif command.upper() == "S":
          if py == 3:
               print("Cannot go down!")
          elif px == bx and py + 1 == by:
               py += 1
               by += 1
          else:
               py += 1
     elif command.upper() == "A":
          if px == 0:
               print("Cannot go left!")
          elif py == by and px - 1 == bx:
               px -= 1
               bx -= 1
          else:
               px -= 1
     elif command.upper() == "W":
          if py == 0:
               print("Cannot go up!")
          elif px == bx and py - 1 == by:
               py -= 1
               by -= 1
          else:
               py -= 1
     elif command.upper() == "R":
          map_game(x, y, px, py, gx, gy, bx, by)
          cmd = input("reset map?")
          if cmd.upper() == "Y":
               print(map_game)
          elif cmd.upper() == "N":
               print()
     else:
          print("Try again!!")
     map_game(x, y, px, py, gx, gy, bx, by)
     
print("You won")
     
  
