import random

user_input = input("")
def roll_dice(sides): #kun lisäät sides parametrin, osaa ohjelma heittää minkä tahansa sivusen nopan kanssa.
    return random.randint(1, sides)

while True:
    roll = roll_dice(10) #10 määrittää nopan sivun, jos olisi 6 olisi kuusisivuinen jne.
    print(roll)
    if roll == 10:
        break