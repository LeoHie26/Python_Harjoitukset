import random

def roll_dice(): #tää määrittää vissiin funktion, jota käytetään ja random.randitilla sit määritetään noppa
    return random.randint(1, 6)

while True: #tää kaiket sit kerää ne heitot kunnes tulee silmäluku 6?
    roll = roll_dice()
    print(roll)
    if roll == 6:
        break