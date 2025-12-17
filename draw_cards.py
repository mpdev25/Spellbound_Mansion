import random
import characters
import items
import locations

def draw_cards(location, character, items):

    room = random.choice(location)

    enemy = random.choice(character)

    loot = random.choice(items)

    return (room, enemy, loot)

location = [locations.room_one, locations.room_two, locations.room_three, locations.room_four, locations.room_five, locations.room_six,  locations.room_seven, locations.room_eight, locations.room_nine, locations.room_ten, locations.room_eleven, locations.room_twelve, locations.room_thirteen, locations.room_fourteen, locations.room_fifteen,locations. room_sixteen, locations.room_seventeen, locations.room_eighteen, locations.room_nineteen, locations.room_twenty]

enemy = [characters.goblin_sword, characters.goblin_bow, characters.skeleton_longbow, characters.skeleton_sword, characters.undead_sorcerer, characters.orc_axe, characters.hellhound, characters.zombie_warrior, characters.zombie_short_bow, characters.specter, characters.ghoul, characters.animated_armour, characters.shadow_lurker, characters.giant_spider, characters.young_giant_spider, characters.lost_bandit, characters.orc_longbow, characters.ogre, characters.horde_of_rats, characters.lich]

loot = [items.wand_of_destruction, items.enhanced_longbow, items.expertly_crafted_longsword, items.great_sword, items.heavy_crossbow, items.staff_of_light, items.sorcerers_tome, items.healing_potion, items.greater_healing_potion, items.potion_of_stone_skin, items.shield_scroll, items.giant_ruby, items.small_chest, items.large_chest, items.pouch, items.sorcerers_horde, items.chainmail_armour, items.plate_armour, items.robe_of_protection, items.small_shield, items.large_shield]