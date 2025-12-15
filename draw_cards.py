import random

def draw_cards(location, character, items):

    room = random.choice(location)

    enemy = random.choice(character)

    loot = random.choice(items)

    return (room, enemy, loot)

location = [room_one, room_two, room_three, room_four, room_five, room_six,  room_seven, room_eight, room_nine, room_ten, room_eleven, room_twelve, room_thirteen, room_fourteen, room_fifteen, room_sixteen, room_seventeen, room_eighteen, room_nineteen, room_twenty]

enemy = [goblin_sword, goblin_bow, skeleton_longbow, skeleton_sword, undead_sorcerer, orc_axe, hellhound, zombie_warrior, zombie_short_bow, specter, ghoul, animated_armour, shadow_lurker, giant_spider, young_giant_spider, lost_bandit, orc_longbow, ogre, horde_of_rats, lich]

loot = [wand_of_destruction, enhanced_longbow, expertly_crafted_longsword, great_sword, heavy_crossbow, staff_of_light, sorcerers_tome, healing_potion, greater_healing_potion, potion_of_stone_skin, shield_scroll, giant_ruby, small_chest, large_chest, pouch, sorcerers_horde, chainmail_armour, plate_armour, robe_of_protection, small_shield, large_shield]