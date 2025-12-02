

class Weapon:
    def __init__(self, category, name, attack, hands, bonus=None):
        self.category = category
        self.name = name
        self.attack = attack
        self.hands = hands
        self.bonus = bonus



class Armour:
    def __init__(self, category, name, protection, bonus=None):
        self.category = category
        self.name = name
        self.protection = protection
        self.bonus = bonus



class MagicItem:
    def __init__(self, name, attack=None, protection=None):
        self.name = name
        self.attack = attack
        self.protection = protection