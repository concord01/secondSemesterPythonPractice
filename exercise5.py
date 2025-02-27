menu = { "Pizza": 1.99, "Soda":  0.69, "Double Chunk Chocolate Chip Cookie": 2.49}

def add_item(item, price):
    menu[item] = price
add_item("Eggs", 4.00)
print(menu)