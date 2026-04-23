items = ["Apple", "Banana", "Peach", "Plum", "Cherry"]
print(items[0])
print(items[1])
print(items[-1])

print(items[:2])
print(items[2:])
print(items[::-1])

for item in items:
    print(item)

items.append("lettuce")
items.append("carrot")
print(items)

items[2] = "Blueberry"
print(items)

items.remove("Apple")
print(items)

item = items.pop(2)
print(item)
print(items)

del items[0:2]
print(items)