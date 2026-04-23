menu = {
    "Pizza": 10,
    "Pasta": 8,
    "Salad": 6,
}
print(menu["Pizza"])

menu["Pasta"] = 12.99
print(menu)

del menu["Salad"]
print(menu)

print(menu.keys())
print(menu.values())
print(menu.items())