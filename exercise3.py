groceries = ["cheez its", "nerds gummy clusters", "doritos", "cocoa puffs", "pepsi", "dr. pepper", "mountain dew"]
print("The grocery list is " + str(groceries))
while True:
    foodRemove = input("What would you like to remove?\n")
    foodRemove.lower()
    if foodRemove == "stop":
        break
    else:
        groceries.remove(foodRemove)
print("Your final grocery list is " + str(groceries))