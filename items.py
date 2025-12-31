
import dice


class Weapon:
    def __init__(self, category, name, dice, damage_roll, hands, bonus):
        self.category = category
        self.name = name
        self.dice = dice
        self.damage_roll = damage_roll
        self.hands = hands
        self.bonus = bonus

    def __str__(self):
        return f"({self.name} Damage: {self.dice})"

   


unarmed = Weapon("melee", "unarmed", "d2", dice.roll_d2, 1, 0)

short_sword = Weapon("melee", "short sword", "d6", dice.roll_d6, 1, 0)

short_bow = Weapon("ranged", "shortbow", "d6", dice.roll_d6, 2, 0)

magic_staff = Weapon("magic", "magic staff", "d6", dice.roll_d6, 2, 0)

long_bow = Weapon("ranged", "longbow", "d8", dice.roll_d8, 2, 1)

long_sword = Weapon("melee", "long sword", "d8", dice.roll_d8, 1, 1)

fire_staff = Weapon("magic", "fire staff", "d20", dice.roll_d20, 2, 5)

great_axe = Weapon("melee", "great axe", "d10", dice.roll_d10, 2, 2)

hellhound_teeth = Weapon("melee", "hellhound teeth", "d10", dice.roll_d10, 2, 0)

spear = Weapon("melee", "spear", "d8", dice.roll_d8, 2, 1)

psychic_blast = Weapon("magic", "psychic blast", "d12", dice.roll_d12, 1, 0)

ghoul_claws = Weapon("melee", "ghoul claws", "d10", dice.roll_d10, 2, 1)

corrosive_spit = Weapon("ranged", "corrosive spit", "d12", dice.roll_d12, 1, 0)

spider_fangs = Weapon("melee", "spider fangs", "d12", dice.roll_d12, 1, 1)

huge_spiked_club = Weapon("melee", "huge spiked club", "d12", dice.roll_d12, 2, 2)

rat_bite = Weapon("melee", "rat bite", "d6", dice.roll_d6, 1, 0)

deathly_touch = Weapon("magic", "deathly touch", "d12", dice.roll_d12, 2, 2)

wand_of_destruction = Weapon("magic", "wand of destruction", "d20", dice.roll_d20, 1, 3)

enhanced_longbow = Weapon("ranged", "enhanced longbow", "d12", dice.roll_d12, 2, 2)

expertly_crafted_longsword = Weapon("melee", "expertly crafted longsword", "d12", dice.roll_d12, 1, 3)

great_sword = Weapon("melee", "great sword", "d12", dice.roll_d12, 2, 3)

heavy_crossbow = Weapon("ranged", "heavy crossbow", "d12", dice.roll_d12, 2, 3)

staff_of_light = Weapon("magic", "staff of light", "d12", dice.roll_d12, 2, 3)

class Armour:
    def __init__(self, category, name, protection):
        self.category = category
        self.name = name
        self.protection = protection

    def __str__(self):
        return f"({self.name} Protection: {self.protection})"
        

leather_armour = Armour("armour", "leather armour", 2)

chainmail_armour = Armour("armour", "chainmail armour", 4)

plate_armour = Armour("armour", "plate armour", 6)

robe_of_protection = Armour("armour", "robe of protection", 10)

small_shield = Armour("shield", "small shield", 2)

large_shield = Armour("shield", "large shield", 4)

class MagicItem:
    def __init__(self, name, life = None, protection=None):
        self.name = name
        self.life = life
        self.protection = protection
             
    def __str__(self):
        return f"({self.name} Life: {self.life} Protection: {self.protection})"


healing_potion = MagicItem("healing potion", 5)

greater_healing_potion = MagicItem("grater healing potion", 10)

potion_of_stone_skin = MagicItem("potion of stone skin", 0, 4)

shield_scroll = MagicItem("scroll of shield", 0, 6)

class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        return f"({self.name} Value: {self.value})"

giant_ruby = Treasure("giant ruby", 50)

small_chest = Treasure("small chest of gold coins", 20)

large_chest = Treasure("large chest of gold and jewels", 100)

pouch = Treasure("pouch of diamonds", 75)

sorcerers_horde = Treasure("the sorcerers hoard", 1000)

sorcerers_tome = Treasure("tome of the sorcerer.", 750)
