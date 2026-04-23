def sum_numbers(a, b):
    return a + b
result = sum_numbers(1,1)
result = sum_numbers(result, 2)
print(result)

GLOBAL_VALUE = "Globally accessible"

def func_one():
    # local_value_one can only be accessed within this function
    local_value_one = "hi"
    print(GLOBAL_VALUE)
    print(f"func_one local value: {local_value_one}")

def func_two():
    # local_value_two can only be accessed within this function
    local_value_two = "hi2"
    print(GLOBAL_VALUE)
    print(f"func_two local value: {local_value_two}")

func_one()
func_two()