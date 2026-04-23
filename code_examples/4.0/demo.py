for i in range(1,11):
    if i == 8:
        break
    if i % 2 == 0:
        print(f"{i} is an even number")
        continue
    print(i)