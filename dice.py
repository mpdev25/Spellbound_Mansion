import random

def roll_dice(sides):
    return random.randint(1, sides)

roll_d6 = roll_dice(6)
print(roll_d6)

roll_d20 = roll_dice(20)
print(roll_d20)

roll_d100 = roll_dice(100)
print(roll_d100)