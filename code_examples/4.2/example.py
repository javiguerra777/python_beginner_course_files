for i in range(100):
    if i == 76:
        print(f"Found target {i}")
        break
    print(i)

for i in range(5):
    if i == 3:
        print(f"filtering out number {i}")
        continue
    print(i)

for i in range(1000):
    pass # pass is used as a placeholder