import random

number = random.randint(1, 10)

while True:
    user_input = int(input("Guess a number (1-10): "))

    if user_input == number:
        print("Correct")
        break

    elif user_input > number:
        print("Too high")

    elif user_input < number:
        print("Too low")