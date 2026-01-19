numbers = []

while True:
    user_input = input("Enter a number: ")

    if user_input == "":
        break

    try:
        number = float(user_input)
        numbers.append(number)

    except ValueError:
        print("Please enter a number")

if numbers:
    numbers.sort(reverse=True)
    print("The greatest numbers in descending order: ")
    for number in numbers[:5]: # jos haluaa rajata numero määrää niin hakasulut ja :numero
        print(number)

else:
    print("No numbers entered")