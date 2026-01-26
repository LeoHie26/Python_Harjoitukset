names = set()

user_input = input("Enter name: ")


def check_name(names):


    if user_input not in names:
        print("Name is new")
        names.add(name)

    else:
        print("Name exist")



print(names)
