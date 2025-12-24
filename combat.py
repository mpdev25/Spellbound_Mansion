from dice import roll_dice
from main import main
import characters
import movement
import items

def roll_initiative(player, enemy):
    print("Roll iniative.")
    player_initiative = roll_dice(20)
    enemy_initiative = roll_dice(20)
    print(f"You roll {player_initiative}!")
    print(f"{enemy.name} rolls {enemy_initiative}!")
    if player_initiative > enemy_initiative:
        return [player, enemy]
    elif enemy_initiative > player_initiative:
        return [enemy, player]
    else:
        return roll_initiative(player, enemy)




def start_battle(turn_order, player):
    first, second = turn_order
    current_turn_index = 0
    participants = [first, second]
    while first.is_alive() and second.is_alive():
        attacker = participants[current_turn_index]
        defender = participants[1 - current_turn_index]
        weapon_category = attacker.weapon.category
        
        if weapon_category == "melee":
            melee_attack(attacker, defender)
        elif weapon_category == "ranged":
            ranged_attack(attacker, defender)
        elif weapon_category == "magic":
            magic_attack(attacker, defender)
            
        if not defender.is_alive():
            print(f"\n{defender.name} has been defeated!")
            
            if defender == player:
                print(f"\n{player.name}, your quest ends here")
                game_running = False
                break

            elif defender != player:

                current_loot = defender.loot
                while True:
                    if isinstance (current_loot, items.Treasure):
                        loot_choice = input(f"To add {current_loot.name} to inventory, press 1, to leave it here, press 3. ")
                        if loot_choice == '1':
                            player.inventory.append(current_loot)
                            print(f"{current_loot.name} added to inventory")
                            print(f"Inventory {attacker.inventory}")
                            break
                        elif loot_choice == '3':
                            print(f"You leave the {current_loot.name} behind")
                            break
                    else:
                        loot_choice = input(f"To add {current_loot.name} to inventory, press 1, to euip it, press 2, to leave it here, press 3. ")
                        if loot_choice == '1':
                            player.inventory.append(current_loot)
                            print(f"{current_loot.name} added to inventory")
                            print(f"Inventory {attacker.inventory}")
                            break
                        elif loot_choice == '2':
                            if isinstance (current_loot, items.Weapon):
                                player.equipped['weapon'] = current_loot
                                print(f"{current_loot.name} equipped")
                                print(f"Equipped items: {attacker.equipped}")
                            if isinstance (current_loot, items.Armour):
                                if current_loot.category == "armour":
                                    player.equipped['armour'] = current_loot
                                    print(f"{current_loot.name} equipped")
                                    print(f"Equipped items: {attacker.equipped}")
                                if current_loot.category == "shield":
                                    player.equipped['shield'] = current_loot
                                    print(f"{current_loot.name} equipped")
                                    print(f"Equipped items: {attacker.equipped}")
                            if isinstance (current_loot, items.MagicItem):
                                player.equipped['magic_item'] = current_loot
                                print(f"{current_loot.name} equipped")
                                print(f"Equipped items: {attacker.equipped}")
                            break
                        elif loot_choice == '3':
                            print(f"You leave the {current_loot.name} behind")
                            break
                        else:
                            print("Invalid input, please enter 1, 2 or 3. ")
            
                current_room, current_enemy, current_loot = movement.direction_choice()
                print(f"You enter a {current_room.name}.")
                print(f"{current_room.description}")
                print(f"In the room you see a {current_enemy.name} and a {current_loot.name}.")
                print(f"The {current_enemy.name} attacks!")
    
                initiate_combat(player, current_enemy)

        current_turn_index = 1 - current_turn_index
    

def melee_attack(attacker, defender):
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.melee_bonus)
    print(f"{attacker.name} rolls {attack}")
    if attack > defender.protection:
        damage_dealt = attacker.weapon.damage
        defender.life -= damage_dealt
        print(f"{defender.name} takes {damage_dealt} damage")
        print(f"{defender.name} has {defender.life} life remaining")




def ranged_attack(attacker, defender):
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.ranged_bonus)
    print(f"{attacker.name} rolls {attack}")
    if attack > defender.protection:
        damage_dealt = attacker.weapon.damage
        defender.life -= damage_dealt
        print(f"{defender.name} takes {damage_dealt} damage")
        print(f"{defender.name} has {defender.life} life remaining")

def magic_attack(attacker, defender):
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.magic_bonus)
    print(f"{attacker.name} rolls {attack}")
    if attack > defender.protection:
        damage_dealt = attacker.weapon.damage
        defender.life -= damage_dealt
        print(f"{defender.name} takes {damage_dealt} damage")
        print(f"{defender.name} has {defender.life} life remaining")

def initiate_combat(player, enemy):
    turn_order = roll_initiative(player, enemy)
    start_battle(turn_order, player)
