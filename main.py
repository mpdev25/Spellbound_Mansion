

from dice import roll_dice
import characters
import combat
import items
import locations
import draw_cards
import movement
import copy
import time


MASTER_LIST_ROOMS = [locations.room_one, locations.room_two, locations.room_three, locations.room_four, locations.room_five, locations.room_six,  locations.room_seven, locations.room_eight, locations.room_nine, locations.room_ten, locations.room_eleven, locations.room_twelve, locations.room_thirteen, locations.room_fourteen, locations.room_fifteen, locations.room_sixteen, locations.room_seventeen, locations.room_eighteen, locations.room_nineteen, locations.room_twenty]

MASTER_LIST_ENEMIES = [characters.goblin_sword, characters.goblin_bow, characters.skeleton_longbow, characters.skeleton_sword, characters.undead_sorcerer, characters.orc_axe, characters.hellhound, characters.zombie_warrior, characters.zombie_short_bow, characters.specter, characters.ghoul, characters.animated_armour, characters.shadow_lurker, characters.giant_spider, characters.young_giant_spider, characters.lost_bandit, characters.orc_longbow, characters.ogre, characters.horde_of_rats, characters.lich]

MASTER_LIST_LOOT = [items.wand_of_destruction, items.enhanced_longbow, items.expertly_crafted_longsword, items.great_sword, items.heavy_crossbow, items.staff_of_light, items.sorcerers_tome, items.potion_of_vitality, items.greater_potion_of_vitality, items.potion_of_stone_skin, items.shield_scroll, items.giant_ruby, items.small_chest, items.large_chest, items.pouch, items.sorcerers_horde, items.chainmail_armour, items.plate_armour, items.robe_of_protection, items.small_shield, items.large_shield]

rooms = []
enemies = []
loot = []

def init_game_data():
    global rooms, enemies, loot
    rooms = copy.deepcopy(MASTER_LIST_ROOMS)

    enemies = copy.deepcopy(MASTER_LIST_ENEMIES)

    loot = copy.deepcopy(MASTER_LIST_LOOT)
    return rooms, enemies, loot

def check_global_commands(user_input, my_player):
    user_input = user_input.lower()
    if user_input == 'q':
        print("Exiting game...")
      
        return False, True
            
      
    if user_input == 't':
        has_tome = any(item.name == "tome of the sorcerer." for item in my_player.inventory)
        if has_tome:
            print("You use the teleport spell in the sorcerers tome to escape Katscurse Mansion.\nTime to check your loot!")
            print("Loot:\n")
            for item in my_player.inventory:
                if hasattr(item, "value"):
                    print(f"{item.name}, {item.value}")
            return False, True
        else:
            print("You don't have a teleport spell!")
            return True, True

    if user_input == 'c':
        characters.character_sheet(my_player)
        return True, True
        
    if user_input == 'e':
        print("\n--- Inventory ---")
        if not my_player.inventory:
            print("your inventory is empty.")
        else:
            print(my_player.display_items(my_player.inventory))

        print("\n--- Equipped ---")
        print(my_player.display_items(my_player.equipped))

        if not my_player.inventory:
            print("\nNothing to equip. Returning to game.")
            return

        while True:
            choice_input = input("Enter the number of the item to equip, or press r to return to game. ").strip().lower()
            if choice_input == 'r':
                print("Returning to game")
                break
            try:
                choice = int(choice_input)
                if 1 <= choice <= len(my_player.inventory):
                    item_to_equip = my_player.inventory[choice - 1]
                    my_player.equip_item(item_to_equip)
                    break
                else:
                    print("Invalid number. Please choose again or press r to return to game.")
            except ValueError:
                print("Invalid input. Please enter a number or r.")
        
        return True, True

    return True, False
       
should_run = True

def stop_game():
    global should_run
    should_run = False
  

def start_new_game(my_player):
    while True:
        user_input = input("Start a new game? y/n ").lower()
     
        if user_input == "y":
            room_list, enemy_list, loot_list = init_game_data()
            return True
        if user_input == "n":
            print("Exiting game.")
            
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
    print("3 Magic combat")

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
    print("The next morning you collect the leather armour and head out to Katscurse mansion, a spring in your step and a smile on your face -- treasure awaits!")
    my_player.inventory.append(items.leather_armour)
    
   
    my_player.equipped['Armour'] = (items.leather_armour)
    my_player.equip_armour = items.leather_armour
    characters.character_sheet(my_player)
   
    print("After a twenty minute walk you reach the Katsscurse mansion. It is a large imposing building, but shows the signs of years of neglect.\nThe entrance gate hangs listlessly on its hinges.")
    print("An overgrown path leads to a large oaken door.")
    print(locations.room_zero.description)
    return my_player

def play_game(my_player, room_list, enemy_list, loot_list):
    game_running = True
    room_list, enemy_list, loot_list = init_game_data()
    while game_running:
        
        user_input = input(f"What do you want to do?\nType q to quit\nType c to view character sheet\nTo equip items from inventory press e\nTo continue through the mansion press m. ")
        should_run, command_handled = check_global_commands(user_input, my_player)
        if not should_run:
            return False
            
     
        if command_handled:
            continue
     
        if user_input == 'm':
           
            result = movement.direction_choice(room_list, enemy_list, loot_list)
            if result is None:
                print("There are no more rooms to explore!")
                final_input = input("Without a teleport spell you are trapped in the mansion forever. If you have the teleport spell use it now, otherwise press q to quit. ").lower()
                continue
            current_room, current_enemy, current_loot = result
            print(f"You enter a {current_room.name}.")
            print(f"{current_room.description}")
            time.sleep(5)
            print(f"In the room you see a {current_enemy.name} and a {current_loot.name}.")
            time.sleep(3)
            print(f"The {current_enemy.name} attacks!")
            time.sleep(2)
            combat.initiate_combat(my_player, current_enemy)
               
            if not my_player.is_alive():
                print("You end just another victim of Katscurse Mansion.")
                return False
                
         
       
        else:
            print("Invalid input. Press q to quit, m to move or c for character sheet")
   



def main():
 
    room_list, enemy_list, loot_list = init_game_data()
    game_running = True
    
    while game_running:
        try:
            my_player = intro(room_list, enemy_list, loot_list)
            game_state = play_game(my_player, room_list, enemy_list, loot_list) 
            game_running = start_new_game(my_player)
        except KeyboardInterrupt:
            break
    
    

if __name__ == "__main__":
    main()