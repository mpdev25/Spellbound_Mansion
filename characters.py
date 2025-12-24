from dice import roll_dice
import items


class Character:
    def __init__(self, name, life, protection, strength, dexterity, magic, weapon, inventory=None, equipped=None, loot = None):
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
        self.inventory = inventory if inventory is not None else []
        self.equipped = equipped if equipped is not None else {'weapon': weapon, 'armour': None, 'Shield': None, 'magic_item': None}
        self.loot = loot if loot is not None else []

    def is_alive(self):
        return self.life > 0


def __str__(self):
    return (
        f"Character: {self.name}\n"
        f"Life: {self.life}\n"
        f"Protection: {self.protection}\n"
        f"Strength: {self.strength}\n"
        f"Dexterity: {self.dexterity}\n"
        f"Magic: {self.magic}\n"
        f"Melee Bonus: {self.melee_bonus}\n"
        f"Ranged Bonus: {self.ranged_bonus}\n"
        f"Magic Bonus: {self.magic_bonus}\n"
        f"Weapon: {self.weapon}\n"
        f"Inventory: {self.inventory}\n"
        f"Equipped: {self.equipped}"
    )

def character_sheet(player):
    print(f"\n--- Character Sheet ---\n{player}")

def get_player_name(player):
    print("\"You're new here, what's your name?\" says a man whose clothing reminds you all too much of your own impoverished upbringing.")
    player.name = input("I'm ")
   
    return player.name


def roll_character():
    strength = roll_dice(6) + roll_dice(6) + roll_dice(6)
    dexterity = roll_dice(6) + roll_dice(6) + roll_dice(6)
    magic = roll_dice(6) + roll_dice(6) + roll_dice(6)

    melee_bonus =  strength // 6
    ranged_bonus = dexterity // 6
    magic_bonus = magic // 6

    total_bonus = melee_bonus + ranged_bonus + magic_bonus
    life = (roll_dice(20) + roll_dice(20)) // 2 + (total_bonus + 100)
    protection = roll_dice(6) + total_bonus
    name = "player"
    starting_weapon = items.unarmed
    inventory = []
    player = Character(
        name = name,
        life = life,
        protection = protection,
        strength = strength,
        dexterity = dexterity,
        magic = magic,
        weapon = starting_weapon,
        inventory = []
    )
    
    return player




def get_weapon(player):
    while True:
        try:
            choice = int(input("Enter your choice: 1, 2 or 3: "))
        
        
            if choice == 1:
                print("You've become adept with the short sword your adventuress aunt left you when she died.")
                player.weapon = items.short_sword
                player.strength += roll_dice(6)
                player.inventory.append(items.short_sword)
                print("Short sword added to inventory")
                break
            elif choice == 2:
                print("You've become adept with the shortbow your adventuress aunt left you when she died")
                player.weapon = items.short_bow
                player.dexterity += roll_dice(6)
                player.inventory.append(items.short_bow)
                print("Short bow added to inventory")
                break
            elif choice == 3:
                print("You've become adept with the magic staff your adventuress aunt left you when she died")
                player.weapon = items.magic_staff
                player.magic += roll_dice(6)
                player.inventory.append(items.magic_staff)
                print("Magic staff added to inventory")
                break
            
            else:
                choice = int(input("Enter your choice: 1, 2 or 3: "))
                
        except ValueError:
            print("Invalid input! Please enter 1, 2 or 3")
            continue



#def equip_weapon():


#def equip_armour():


#def use_item():


goblin_sword = Character("goblin with a shortsword", 6, 6, 6, 6, 6, items.short_sword)

goblin_bow = Character("goblin with a shortbow", 6, 6, 6, 6, 6, items.short_bow)

skeleton_longbow = Character("skeleton with a longbow", 8, 10, 7, 12, 5, items.long_bow)

skeleton_sword = Character("skeleton with a longsword", 8, 10, 12, 7, 5, items.long_sword)

undead_sorcerer= Character("undead sorcerer", 20, 18, 12, 12, 18, items.fire_staff)

orc_axe = Character("orc with a greataxe", 12, 12, 12, 12, 5, items.great_axe)

hellhound = Character("hellhound", 14, 12, 18, 18, 8, items.hellhound_teeth)

zombie_warrior = Character("zombie with a spear", 10, 12, 15, 14, 7, items.spear)

zombie_short_bow = Character("zombie with a shortbow", 10, 12, 14, 15, 7, items.short_bow)

specter = Character("specter", 14, 14, 8, 12, 18, items.psychic_blast)

ghoul = Character("ghoul", 12, 12, 16, 14, 12, items.ghoul_claws)

animated_armour = Character("animated armour", 12, 18, 16, 12, 8, items.long_sword)

shadow_lurker = Character("shadodw lurker", 14, 20, 10, 18, 18, items.corrosive_spit)

giant_spider = Character("giant spider", 16, 14, 14, 16, 6, items.spider_fangs)

young_giant_spider = Character("young giant spider", 10, 10, 8, 10, 6, items.spider_fangs)

lost_bandit = Character("lost bandit", 12, 12, 12, 12, 12, items.short_sword)

orc_longbow = Character("orc with a longbow", 12, 12, 12, 12, 5, items.long_bow)

ogre = Character("ogre with a huge spiked club", 18, 16, 18, 14, 8, items.huge_spiked_club)

horde_of_rats = Character("horde of rats", 20, 10, 6, 12, 2, items.rat_bite)

lich = Character("lich", 20, 20, 18, 12, 18, items.deathly_touch)
