

class Character:
    def __init__(self, name, life, protection, strength, dexterity, magic):
        self.name = name
        self.life = life
        self.protection = protection
        self.strength = strength
        self.dexterity = dexterity
        self.magic = magic

player_character = Character()

goblin = Character("goblin", 10, 11, 12, 14, 8)