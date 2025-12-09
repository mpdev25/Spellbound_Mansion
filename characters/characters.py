from main import get_player_name
from dice import roll_dice
from items import Weapon


class Character:
    def __init__(self, name, life, protection, strength, dexterity, magic, melee_bonus, ranged_bonus, magic_bonus, weapon=None):
        self.name = name
        self.life = life
        self.protection = protection
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic
        self.melee_bonus = melee_bonus
        self.ranged_bonus = ranged_bonus
        self.magic_bonus = magic_bonus
        self.weapon = weapon

def roll_character():
    player = Character()
    self.name = name
    self.life = (roll_dice(20) + roll_dice(20)) // 2 + (melee_bonus + ranged_bonus + magic_bonus)
    self.protection = roll_dice(6) + (melee_bonus + ranged_bonus + magic_bonus)
    self.strength = roll_dice(6) + roll_dice(6) + roll_dice(6)
    self.dexterity = roll_dice(6) + roll_dice(6) + roll_dice(6)
    self.magic = roll_dice(6) + roll_dice(6) + roll_dice(6)
    self.melee_bonus =  strength // 6
    self.ranged_bonus = dexterity // 6
    self.magic_bonus = magic // 6
    self.weapon = weapon

goblin_sword = Character("goblin", 6, 6, 6, 6, 6, 1, 1, 1, short_sword)

goblin_bow = Character("goblin", 6, 6, 6, 6, 6, 1, 1, 1, short_bow)

skeleton_longbow = Character("skeleton", 8, 10, 7, 12, 5, 1, 2, 1, long_bow)

