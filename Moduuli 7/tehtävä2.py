def check_name(name):
    if name in names:
        print("Existing name.")


    else:
        names.add(name)
        print("New name.")

names = set()

while True:

    user_input = input("Enter name to the list: ")

    if user_input == "":
        break

    check_name(user_input)

for name in names:
    print(name)