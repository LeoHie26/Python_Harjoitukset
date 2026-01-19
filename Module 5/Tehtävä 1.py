import random

dice_amount = int(input("How many dice to roll: "))
total = 0

for i in range(dice_amount):
    throw = random.randint(1, 6)
    total += throw

print(f"Sum of the dice: {total}")
