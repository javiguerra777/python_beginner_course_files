try:
    first_num = int(input("Input first number to divide by (EX: 1): "))
    second_num = int(input("Second number to divide by (EX: 2): "))
    result = first_num / second_num
except ValueError:
    print("Error trying to convert input to integer, please make sure to pass a valid whole number such as 1 or 2")
except ZeroDivisionError:
    print("You cannot divide by 0, check your input and run program again")
else:
    print(f"Result of division {result}")
finally:
    print("Program is done executing, Goodbye!")