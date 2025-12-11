
from dice import roll_dice
from items import Weapon


class Character:
    def __init__(self, name, life, protection, strength, dexterity, magic, weapon=None):
        self.name = name
        self.life = life
        self.protection = protection
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic
        self.melee_bonus = strength // 6
        self.ranged_bonus = dexterity // 6
        self.magic_bonus = magic // 6
        self.weapon = weapon

def get_player_name():
    print("\"Your new here, what's your name?\" says a man whose clothing reminds you all too much of your own impoverished upbringing.")
    player_name = input("I'm ")
    return player_name
    

def roll_character():
    strength = roll_dice(6) + roll_dice(6) + roll_dice(6)
    dexterity = roll_dice(6) + roll_dice(6) + roll_dice(6)
    magic = roll_dice(6) + roll_dice(6) + roll_dice(6)

    melee_bonus =  strength // 6
    ranged_bonus = dexterity // 6
    magic_bonus = magic // 6

    total_bonus = melee_bonus + ranged_bonus + magic_bonus
    life = (roll_dice(20) + roll_dice(20)) // 2 + total_bonus
    protection = roll_dice(6) + total_bonus
    name = get_player_name()

    player = Character(
        name = name
        life = life
        protection = protection
        strength = strength
        dexterity = dexterity
        magic = magic
        weapon = weapon
    )
    return player

goblin_sword = Character("goblin", 6, 6, 6, 6, 6, short_sword)

goblin_bow = Character("goblin", 6, 6, 6, 6, 6, short_bow)

skeleton_longbow = Character("skeleton", 8, 10, 7, 12, 5, long_bow)

