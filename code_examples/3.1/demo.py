rating = float(input("What is your rating on a scale from 1-10 for the movie titled EXAMPLE? "))
if rating >= 9.0:
    label = "Excellent"
elif rating >= 7.0:
    label = "Good"
else:
    label = "Poor"

print(f"The movie EXAMPLE is {label}")