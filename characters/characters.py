from main import get_player_name roll_character

class Character:
    def __init__(self, name=None, life, protection, strength, dexterity, magic, melee_bonus, ranged_bonus, magic_bonus, weapon=None):
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

player = roll_character(player_name)

goblin = Character("goblin", 10, 11, 12, 14, 8)