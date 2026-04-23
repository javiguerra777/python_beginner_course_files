first_num = int(input("Input first number to divide by: "))
second_num = int(input("Input second number to divide by: "))
try:
    print(f"Result: {first_num / second_num}")
except ZeroDivisionError:
    print("Tried dividing by zero, you cannot divide by zero")
else:
    print("SUCCESSFUL DIVISION ATTEMPT")
finally:
    print("RUNNING CLEANUP ACTION")