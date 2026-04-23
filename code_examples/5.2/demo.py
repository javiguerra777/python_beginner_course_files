data = {
    "name": "User",
    "company": "Company",
    "role": "intern",
}
print(data["name"])
data["role"] = "Project Manager"
data["email"] = "email@placeholder.com"
data["location"] = {
    "city": "Miami",
    "state": "FL"
}
for item in data.items():
    if item[0] == "location":
        print(f"{item[0]}: {item[1]["city"]}, {item[1]["state"]}")
    else:
        print(f"{item[0]}: {item[1]}")