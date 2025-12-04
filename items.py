

class Weapon:
    def __init__(self, category, name, attack, damage, hands, bonus=None):
        self.category = category
        self.name = name
        self.attack = attack
        self.damage = damage
        self.hands = hands
        self.bonus = bonus



class Armour:
    def __init__(self, category, name, protection, bonus=None):
        self.category = category
        self.name = name
        self.protection = protection
        self.bonus = bonus



class MagicItem:
    def __init__(self, name, attack=None, damage=None, protection=None):
        self.name = name
        self.attack = attack
        self.damage = damage
        self.protection = protection