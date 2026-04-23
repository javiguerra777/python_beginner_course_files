full_name = "John Cool Doe"
split_name = full_name.split(" ")
formatted_name = f"{split_name[0]} {split_name[1][0]}. {split_name[2]}"
print(formatted_name.upper())
message = "   Hello I am an evil pizza overlord     "
print(message.strip().replace("evil", "good"))
secret_message = "egassem terces a dnif ot em esrever"
print(secret_message[::-1])
multi_message = "Hello World 1st line\nSecond line something else\nFinal line with a goodbye"
print(multi_message)