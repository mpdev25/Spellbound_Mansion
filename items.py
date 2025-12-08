from dice import roll_dice

class Weapon:
    def __init__(self, category, name, damage, hands, bonus=None):
        self.category = category
        self.name = name
        self.damage = damage
        self.hands = hands
        self.bonus = bonus

    short_sword = Weapon("melee", "short sword", roll_dice(6), 1)

    short_bow = Weapon("ranged", "shortbow", roll_dice(6), 2)

    magic_staff = Weapon("magic", "magic staff", roll_dice(6), 2)



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