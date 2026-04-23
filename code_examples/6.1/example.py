def greet_user(name):
    print(f"Hello World, {name}")

greet_user("John Doe")

def add_numbers(a=1, b=2):
    result = a + b
    print(result)

add_numbers()
add_numbers(a=11, b=12)