username = "yoyo"
password = "secret"
if username == "yoyo" and password == "secret":
    print("Login Successful!")
else:
    print("Incorrect credentials")

is_member = False
has_ticket = True
if is_member or has_ticket:
    print("You can enter")
else:
    print("Entrance DENIED!")

day_of_week = "Tuesday"
if not (day_of_week == "Saturday" or day_of_week == "Sunday"):
    print("It's a weekday")
else:
    print("It's a weekend")