from dice import roll_dice
import characters
import combat
import items
import locations
import draw_cards
import movement

def start_new_game():
    while True:
        user_input = input("Start a new game? y/n ").lower()
        if user_input == "y":
            return True
        if user_input == "n":
            return False
        else:
            print("Invalid input, please enter y or n.")
            continue

    


def intro(room_list, enemy_list, loot_list):
    print("In the warm, cozy confines of the Drunken Demigorgan Tavern, the only watering hole in Snagleback village, you contemplate the choices that led you here and the future that awaits.")
    print("Before leaving your village you spent a year training in secret to prepare for a life of adventure and, you hope, riches!")
    print("You focused your training on")
  

    my_player = characters.roll_character()

    print("1 Melee combat")
    print("2 Ranged combat")
    print("3 magic combat")

    characters.get_weapon(my_player)
    
        
    print("As you sit finishing your ale and contemplating your next move you overhear some interesting conversation concerning an abandoned mansion not far from Snagleback village.")
    print("You turn to the people talking at the table next to you to learn more.")
    
    my_player.name = characters.get_player_name(my_player)

    print("\"I couldn't help but hear you talking of a mysterious mansion nearby\"")
    print("\"The old Katscurse mansion, it's just a mile North of here, but I wouldn't go there if I was you\" the man says as his companions nod.")
    print("\"It belonged to the sorcerer, Paskratos, but he hasn't been seen for fifty years. Some unwise people have enterd the mansion over the years in search of riches, but none has ever been seen again.\"")
    print("The man looks at you thoughtfully for a moment, studying the keen interest in the mansion that the look on your face betrays.")
    print("Finally he lets out a sigh and exclaims \"I can see you are an unwise person. At least wait till the morning and I will give you my old fathers leather armour. I doubt it will help much, but better than nothing perhaps.\"")
    print(".......")
    print("The next morning you collect the leather armour and head out to Katscurse mansion, a spring in your step adn a smile on your face -- treasue awaits!")
    my_player.inventory.append(items.leather_armour)
    characters.character_sheet(my_player)
    
    print("After a twenty minute walk you reach the Katsscurse mansion. It is a large imposing building, but shows the signs of years of neglect. The entrance gate hangs listlessly on its hinges.")
    print("An overgrown path leads to a large oaken door.")
    print(locations.room_zero.description)

    current_room, current_enemy, current_loot = movement.direction_choice()
    

    print(f"You enter a {current_room.name}.")
    print(f"{current_room.description}")
    print(f"In the room you see a {current_enemy.name} and a {current_loot.name}.")
    print(f"The {current_enemy.name} attacks!")
    #current_turn_order = combat.roll_initiative(my_player, current_enemy)
    #current_fight = combat.start_battle(current_turn_order)
    combat.initiate_combat(my_player, current_enemy)


def main():
    room_list = [locations.room_one, locations.room_two, locations.room_three, locations.room_four, locations.room_five, locations.room_six,  locations.room_seven, locations.room_eight, locations.room_nine, locations.room_ten, locations.room_eleven, locations.room_twelve, locations.room_thirteen, locations.room_fourteen, locations.room_fifteen, locations.room_sixteen, locations.room_seventeen, locations.room_eighteen, locations.room_nineteen, locations.room_twenty]

    enemy_list = [characters.goblin_sword, characters.goblin_bow, characters.skeleton_longbow, characters.skeleton_sword, characters.undead_sorcerer, characters.orc_axe, characters.hellhound, characters.zombie_warrior, characters.zombie_short_bow, characters.specter, characters.ghoul, characters.animated_armour, characters.shadow_lurker, characters.giant_spider, characters.young_giant_spider, characters.lost_bandit, characters.orc_longbow, characters.ogre, characters.horde_of_rats, characters.lich]

    loot_list = [items.wand_of_destruction, items.enhanced_longbow, items.expertly_crafted_longsword, items.great_sword, items.heavy_crossbow, items.staff_of_light, items.sorcerers_tome, items.healing_potion, items.greater_healing_potion, items.potion_of_stone_skin, items.shield_scroll, items.giant_ruby, items.small_chest, items.large_chest, items.pouch, items.sorcerers_horde, items.chainmail_armour, items.plate_armour, items.robe_of_protection, items.small_shield, items.large_shield]
    game_running = True
    while game_running:
        game_state = intro(room_list, enemy_list, loot_list) 
        game_running = start_new_game()



if __name__ == "__main__":
    main()