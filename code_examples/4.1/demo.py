correct_password = "python123"
max_attempts = 3
success = False

while max_attempts > 0:
    print(f"You have {max_attempts} left to guess correct password")
    user_input = input("What is the correct password? ")
    if user_input == correct_password:
        success = True
        break
    max_attempts -= 1

if success:
    print("You were CORRECT")
else:
    print("You LOST, please try again")