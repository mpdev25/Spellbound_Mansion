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

long_bow = Weapon("ranged", "longbow", roll_dice(8), 2, 1)

long_sword = Weapon("melee", "long sword", roll_dice(8), 1, 1)

fire_staff = Weapon("magic", "fire staff", roll_dice(20), 2, 5)

great_axe = Weapon("melee", "great axe", roll_dice(10), 2, 2)

hellhound_teeth = Weapon("melee", "hellhound teeth", roll_dice(10), 2)

spear = Weapon("melee", "spear", roll_dice(8), 2, 1)

psychic_blast = Weapon("magic", "psychic blast", roll_dice(12), 1)

ghoul_claws = Weapon("melee", "ghoul claws", roll_dice(10), 2, 1)

corrosive_spit = Weapon("ranged", "corrosive spit" roll_dice(12), 1)

spider_fangs = Weapon("melee", "spider fangs", roll_dice(12), 1, 1)

huge_spiked_club = Weapon("melee", "huge spiked club", roll_dice(12), 2, 2)

rat_bite = Weapon("melee", "rat bite", roll_dice(6), 1)

deathly_touch = Weapon("magic", "deathly touch", roll_dice(12), 2, 2)

wand_of_destruction = Weapon("magic", "wand of destruction", roll_dice(20), 1, 3)

enhanced_longbow = Weapon("ranged", "enhanced longbow", roll_dice(12), 2, 2)

expertly_crafted_longsword = Weapon("melee", "expertly crafter longsword", roll_dice(12), 1, 3)

great_sword = Weapon("melee", "great sword", roll_dice(12), 2, 3)

heavy_crossbow = Weapon("ranged", "heavy crossbow", roll_dice(12), 2, 3)

staff_of_light = Weapon("magic", "staff of light", roll_dice(12), 2, 3)

class Armour:
    def __init__(self, category, name, protection):
        self.category = category
        self.name = name
        self.protection = protection
        

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
             

sorcerers_tome = MagicItem("tome of the sorcerer")

healing_potion = MagicItem("healing potion", 5)

greater_healing_potion = MagicItem("grater healing potion", 10)

potion_of_stone_skin = MagicItem("potion of stone skin", 0, 4)

shield_scroll = MagicItem("scroll of shield", 0, 6)

class Treasure:
    def __init__(self, name, value):
        self.name = name
        self.value = value

giant_ruby = Treasure("giant ruby", 50)

small_chest = Treasure("small chest of gold coins", 20)

large_chest = Treasure("large chest of gold and jewels", 100)

pouch = Treasure("pouch of diamonds", 75)

sorcerers_horde = Treasure("the sorcerers hoard", 1000)
