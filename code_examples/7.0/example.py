# Reading from .txt examples
with open("example.txt") as file:
    print(file.read())

with open("example.txt") as file:
    print(file.readlines())

# Writing to .txt example
with open("output.txt", "w") as file:
    message = "Hello World!"
    file.write(message)

import csv
# Reading from .csv examples
with open("example.csv", mode="r", newline="") as file:
    reader = csv.reader(file)
    for row in reader:
        # have to use array indexing to get specific data
        print(row)
# Reading from .csv examples
with open("example.csv", mode="r", newline="") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # have to use key value pairs to get specific data
        print(row["Name"])

# writing to .csv examples
data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "New York"],
    ["Bob", 31, "Chicago"]
]
with open("output.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # using writerows
    writer.writerows(data)
    # iteration example with writerow
    # for row in data:
    #     writer.writerow(row)

dict_data = [
    {"Breed": "Corgi", "Name": "Coolio"},
    {"Breed": "Husky", "Name": "Mr.Floofs"}
]
with open("output.csv", mode="w", newline="") as file:
    field_names = ["Breed", "Name"]
    writer = csv.DictWriter(file, fieldnames=field_names)
    writer.writeheader()
    writer.writerows(dict_data)