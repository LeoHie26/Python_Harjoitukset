user_name = "python"
user_password = "rules"

attempts = 0
max_attempts = 5
while attempts < max_attempts:
    user = input("Enter username: ")
    password = input ("Enter password: ")

    if user == user_name and password == user_password:
        print("Welcome")
        break

    attempts += 1
    if attempts < max_attempts:
        print("Incorrect username or password. Please try again.")

if attempts == max_attempts:
    print("Access denied")



