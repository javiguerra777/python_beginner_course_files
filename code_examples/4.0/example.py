items = ["Jacket", "Hot Dog", "Gold Medal"]
for item in items:
    print(item)

for i in range(10):
    print(i)

for i in range(20):
    if i == 5:
        print("Found 5!")
        break
    print(i)

for i in range(20):
    if i % 2 == 0:
        print("Even Number")
        continue
    print(i)