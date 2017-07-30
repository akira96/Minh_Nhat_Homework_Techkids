clothes = ["T-Shirt", "Sweater"]
print("Hello, welcome to my shop\n")
while (True):
        command = input("Welcome to our shop, what do you want (C, R, U, D)? ")
        if command.upper() == "C":
                new_item = input("Enter new item: ")
                clothes.append(new_item.capitalize())
        elif command.upper() == "R":
                print(end='')
        elif command.upper() == "U":
                pos = int(input("Update position? "))
                if pos <= len(clothes):
                        new_item = input("Enter new item: ")
                        clothes[pos-1] = new_item.capitalize()
                else:
                        print("Sorry, your item is out of sale!")
        elif command.upper() == "D":
                pos = int(input("Delete position? "))
                if pos <= len(clothes):
                        clothes.pop(pos-1)
                else:
                        print("Sorry, your item is out of sale!")
        else:
                print("Oops! We're in reconstructing and can't serve you. See ya!")
	
        print("Our items: ",end='')
        for item in clothes:
                if clothes.index(item) < len(clothes) - 1:
                        print(item,end=', ')
                else:
                        print(item+"\n")
		
