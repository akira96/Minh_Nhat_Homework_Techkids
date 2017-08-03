inventory = {
    'gold' : 500,
    'pouch' : ['flint', 'twine', 'gemstone'],
    'backpack' : ['xylophone', 'dagger', 'bedroll', 'bread loaf']
    }
print("Inventory :", inventory)

inventory["pocket"] = ["seashell", "strange berry", "lint"]
print("Pocket: ", inventory["pocket"])

inventory["backpack"].sort()
print("Backpack: ", inventory["backpack"])

del inventory["backpack"][inventory["backpack"].index('dagger')]
print("Backpack: ", inventory["backpack"])

inventory["gold"] += 50
print("Gold: ", inventory["gold"])

input()

