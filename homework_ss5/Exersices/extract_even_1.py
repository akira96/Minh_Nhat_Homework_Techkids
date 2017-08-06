
print("Cho tap hop: [1, 4, 5, -1, 10]")
import time
time.sleep(1)
print("Viet tap hop so chan?")
time.sleep(1)

def so_chan(numbers):
     so_chan = [number for number in numbers if number%2 == 0]
     print(so_chan)
     return so_chan

so_chan([1,4,5,-1,10])
     
input()
