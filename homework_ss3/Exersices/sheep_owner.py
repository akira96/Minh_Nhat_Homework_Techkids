from random import *

month = 5
total_size = 0
biggest_sheep = 0
sheep_price = 5
flock_sz = []

for i in range(9):
        flock_sz.append(randint(5,300))
print("Hello, my name is Nhat and this is my sheep size:")
print(flock_sz)
biggest_sheep = max(flock_sz)
print("Now my biggest sheep size is {}, let's shear it now!".format(biggest_sheep))
flock_sz[flock_sz.index(biggest_sheep)] = 8
print("After shear that sheep, here is my flock now")
print(flock_sz)
print("\n")

for i in range(month):
        print("MONTH {} :".format(i+1))
        print("One month pass, here is my flock now")
        for i in range(len(flock_sz)):
                flock_sz[i] += 50
        print(flock_sz)
        biggest_sheep = max(flock_sz)
        print("Now my biggest sheep size is {}, let's shear it now!".format(biggest_sheep))
        flock_sz[flock_sz.index(biggest_sheep)] = 8
        print("After shear that sheep, here is my flock now")
        print(flock_sz)
        print("\n")
for item in flock_sz:
        total_size += item

print("My flock total size is: {}".format(total_size))
print("I'll get {0}$ * {1}$ = {2}$".format(total_size,sheep_price,total_size*sheep_price))
input()
