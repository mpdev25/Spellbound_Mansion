
from dice import roll_dice
from items import Weapon, short_sword, short_bow, magic_staff, long_bow, long_sword, fire_staff, great_axe, hellhound_teeth, spear


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
    return (
        f"Character: {self.name}\n"
        f"Life: {self.life}\n"
        f"Protection: {self.protection}\n"
        f"Strength: {self.strength}\n"
        f"Dexterity: {self.dexterity}\n"
        f"Magic: {self.magic}\n"
        f"Weapon: {self.weapon}")

def get_player_name(player):
    print("\"You're new here, what's your name?\" says a man whose clothing reminds you all too much of your own impoverished upbringing.")
    player_name = input("I'm ")
    print(f"\n--- Character Sheet ---\n{str(player)}")
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

def get_weapon(player):
    while True:
        try:
            choice = int(input("Enter your choice: 1, 2 or 3: "))
        
        
            if choice == 1:
                print("You've become adept with the short sword your adventuress aunt left you when she died.")
                player.weapon = short_sword
                break
            elif choice == 2:
                print("You've become adept with the shortbow your adventuress aunt left you when she died")
                player.weapon = short_bow
                break
            elif choice == 3:
                print("You've become adept with the magic staff your adventuress aunt left you when she died")
                player.weapon = magic_staff
                break
            
            else:
                choice = int(input("Enter your choice: 1, 2 or 3: "))
                
        except ValueError:
            print("Invalid input! Please enter 1, 2 or 3")

goblin_sword = Character("goblin with a shortsword", 6, 6, 6, 6, 6, short_sword)

goblin_bow = Character("goblin with a shortbow", 6, 6, 6, 6, 6, short_bow)

skeleton_longbow = Character("skeleton with a longbow", 8, 10, 7, 12, 5, long_bow)

skeleton_sword = Character("skeleton with a longsword", 8, 10, 12, 7, 5, long_sword)

undead_sorcerer= Character("undead sorcerer", 20, 18, 12, 12, 18, fire_staff)

orc_axe = Character("orc with a greataxe", 12, 12, 12, 12, 5, great_axe)

hellhound = Character("hellhound", 14, 12, 18, 18, 8, hellhound_teeth)

zombie_warrior = Character("zombie with a spear", 10, 12, 15, 14, 7, spear)

zombie_short_bow = Character("zombie with a shortbow", 10, 12, 14, 15, 7, short_bow)

specter = Character("specter", 14, 14, 8, 12, 18, psychic_blast)

ghoul = Character("ghoul", 12, 12, 16, 14, 12, ghoul_claws)

animated_armour = Character("animated armour", 12, 18, 16, 12, 8, long_sword)

shadow_lurker = Character("shadodw lurker" 14, 20, 10, 18, 18, corrosive_spit)

giant_spider = Character("giant spider", 16, 14, 14, 16, 6, spider_fangs)

young_giant_spider = Character("young giant spider", 10, 10, 8, 10, 6, spider_fangs)

lost_bandit = Character("lost bandit", 12, 12, 12, 12, 12, short_sword)

orc_longbow = Character("orc with a longbow", 12, 12, 12, 12, 5, long_bow)

 ogre = Character("ogre with a huge spiked club", 18, 16, 18, 14, 8, huge_spiked_club)

horde_of_rats = Character("horde of rats", 20, 10, 6, 12, 2, rat_bite)

lich = Character("lich", 20, 20, 18, 12, 18, deathly_touch)
