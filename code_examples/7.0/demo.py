import csv
data = [
    ['User', 'Status']
]
with open("demo.txt", "r") as file:
    for idx, line in enumerate(file.readlines()):
        sanitized_line = line.strip()
        if idx != 0:
            data.append(sanitized_line.split(" "))

with open("demo.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    # method to write all rows at once
    writer.writerows(data)
    # method to use iteration to write row
    # BOTH methods work
    # for row in data:
    #     writer.writerow(row)

print("TASK COMPLETE TOOK DATA FROM demo.txt FILE AND CONVERTED IT TO demo.csv file")