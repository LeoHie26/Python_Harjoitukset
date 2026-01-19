import random

user_input = input("")
def roll_dice():
    return random.randint(1, user_input)


while True:
    roll = roll_dice()
    print(roll)
    if roll == user_input:
        break