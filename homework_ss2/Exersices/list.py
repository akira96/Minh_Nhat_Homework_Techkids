lolipop_list = []

lolipop_list.append("strawberry")
lolipop_list.append("chocolate")
lolipop_list.append("cocacola")

print("Hello, welcome to my Lolipop Shop")

for i in lolipop_list:
    #string format
    print("{0}. {1}".format(lolipop_list.index(i) +1, i))
    

item = input("which one?")
if item in lolipop_list:
    lolipop_list.remove(item)
else:
    #TODO: Do you mean...
    print("Sorry, we're out of", item)
print(lolipop_list)

#index
