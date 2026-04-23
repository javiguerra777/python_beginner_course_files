BONUS_PERCENTAGE = 0.05
name = input("What is your name? ")
base_salary = float(input("What is your annual salary in USD? "))
increased_salary = base_salary + (base_salary * BONUS_PERCENTAGE)
print(f"{name} makes {base_salary:.2f} this year, and next year will make {increased_salary:.2f}")