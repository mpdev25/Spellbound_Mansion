import random

def roll_dice(sides):
    return random.randint(1, sides)

def roll_d2():
    return roll_dice(2)

def roll_d6():
    return roll_dice(6)

def roll_d8():
    return roll_dice(8)

def roll_d10():
     return roll_dice(10)

def roll_d12():
    return roll_dice(12)

def roll_d20():
    return roll_dice(20)