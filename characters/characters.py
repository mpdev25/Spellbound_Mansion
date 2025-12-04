

class Character:
    def __init__(self, name, life, protection, strength, dexterity, magic, melee_bonus, ranged_bonus, magic_bonus, weapon):
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

player_character = Character()

goblin = Character("goblin", 10, 11, 12, 14, 8)