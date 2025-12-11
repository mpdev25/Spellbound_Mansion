
from dice import roll_dice
from items import Weapon, short_sword, short_bow, magic_staff, long_bow, long_sword, fire_staff, great_ax, hellhound_teeth


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

def __str__(self):
    return (f"Character: {self.name}\n"
            f" Life: {self.life}\n"
            f" Protection: {self.protection}\n"
            f" Strength: {self.strength}\n"
            f" Dexterity: {self.dexterity}\n"
            f" Magic: {self.magic}\n"
            f" Weapon: {self.weapon}")

def get_player_name():
    print("\"You're new here, what's your name?\" says a man whose clothing reminds you all too much of your own impoverished upbringing.")
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
    name = "player"

    player = Character(
        name = name,
        life = life,
        protection = protection,
        strength = strength,
        dexterity = dexterity,
        magic = magic,
        weapon = Weapon
    )
    
    return player



goblin_sword = Character("goblin with a shortsword", 6, 6, 6, 6, 6, short_sword)

goblin_bow = Character("goblin with a shortbow", 6, 6, 6, 6, 6, short_bow)

skeleton_longbow = Character("skeleton with a longbow", 8, 10, 7, 12, 5, long_bow)

skeleton_sword = Character("skeleton with a longsword", 8, 10, 12, 7, 5, long_sword)

undead_sorcerer= Character("undead sorcerer", 20, 18, 12, 12, 18, fire_staff)

orc_ax= Character("orc with a greatax", 12, 12, 12, 12, 5, great_ax)

hellhound = Character("hellhound", 14, 12, 18, 18, 8, hellhound_teeth)

#= Character("")

#= Character("")

#= Character("")

#= Character("")

#= Character("")

#= Character("")

#= Character("")

#= Character("")

#= Character("")

#= Character("")

#= Character("")

#= Character("")

#= Character("")
