menu = ["margarita", "pepperoni", "hawaiian", "veggie", "meat_lovers"]
stock = {"margarita": 20, "pepperoni": 15, "hawaiian": 7, "veggie": 4, "meat_lovers": 1}
price = {"margarita": 120, "pepperoni": 150, "hawaiian": 145, "veggie": 110, "meat_lovers": 175}

total_stock = 0
for item in menu:
    item_value = stock[item] * price[item]
    total_stock += item_value

print(f"Total stock value: R{total_stock}")