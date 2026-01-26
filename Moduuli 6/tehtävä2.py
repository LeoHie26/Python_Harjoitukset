import random

user_input = int(input("Enter a number: "))
def roll_dice(sides): #kun lisäät sides parametrin, osaa ohjelma heittää minkä tahansa sivusen nopan kanssa.
    return random.randint(1, sides)

while True:
    roll = roll_dice(user_input) #määrittää nopan sivun, jos olisi 6 olisi kuusisivuinen jne.
    print(roll)
    if roll == user_input:
        break