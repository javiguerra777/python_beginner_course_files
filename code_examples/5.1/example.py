# tuple code examples
items = ("apple", "banana", "cherry")
print(items)

print(items[0])

for item in items:
    print(item)

# set code examples
unique_list = set(["joe", "h", "john"])
print(unique_list)

unique_list.add("new")
unique_list.update(["1", "2"])
print(unique_list)

unique_list.remove("h")
unique_list.discard("nothing")
print(unique_list)

for item in unique_list:
    print(item)

if "joe" in unique_list:
    print("joe exists!")