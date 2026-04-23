with open("log_file.txt", "r") as file:
    print(file.read())

if file.closed:
    print("File Closed!")
else:
    print("File is still open, please close the file in your code")