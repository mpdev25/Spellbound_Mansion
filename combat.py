from dice import roll_dice
from main import stop_game, start_new_game, should_run
import characters
import movement
import items

def initiate_combat(player, enemy):
    turn_order = roll_initiative(player, enemy)
    start_battle(turn_order, player)

def roll_initiative(player, enemy):
    print("Roll iniative.")
    while True:
        player_initiative = roll_dice(20)
        enemy_initiative = roll_dice(20)
        print(f"You roll {player_initiative}!")
        print(f"{enemy.name} rolls {enemy_initiative}!")
        if player_initiative > enemy_initiative:
            return [player, enemy]
        elif enemy_initiative > player_initiative:
            return [enemy, player]
        else:
            print("A tie! Rolling again...")




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
            check_defender_state(player, defender)
            
 #           if defender == player:
  #              print(f"\n{player.name}, your quest ends here")
   #             stop_game()
               # break

    #        elif defender != player:

     #           current_loot = defender.loot
       #         while True:
        #            if isinstance (current_loot, items.Treasure):
         #               if current_loot.name == "tome of the sorcerer.":
          #                  print("The tome contains many spells, but of particular interest is a teleportation spell you could use to leave the mansion.")
       #                     escape = input("Press t to teleport out of the mansion. You can also press t later if you do not wish to leave now. ").lower()
        #                    if escape == 't':
         #                       print("You use the spell in the sorcerers tome to teleport yourself out of Katscurse Mansion.\nCongratulations, you have survived!")
          #                      main.game_running = False
          #                      return
           #             loot_choice = input(f"To add {current_loot.name} to inventory, press 1, to leave it here, press 3. ")
         #               if loot_choice == '1':
          #                  player.inventory.append(current_loot)
           #                 print(f"{current_loot.name} added to inventory")
          #                  print(f"Inventory {attacker.inventory}")
          #                  break
           #             elif loot_choice == '3':
            #                print(f"You leave the {current_loot.name} behind")
            #                break
             #           else:
              #              print("Invalid input. Please enter 1 or 3")
              #              continue
              #      else:
               #         loot_choice = input(f"To add {current_loot.name} to inventory, press 1, to euip it, press 2, to leave it here, press 3. ")
                #        if loot_choice == '1':
                 #           player.inventory.append(current_loot)
                 #           print(f"{current_loot.name} added to inventory")
                  #          print(f"Inventory {attacker.inventory}")
                   #         break
             #           elif loot_choice == '2':
                                        
              #              if isinstance (current_loot, items.Weapon):
               #                 player.equipped['Weapon'] = current_loot
                #                player.weapon = current_loot
                 #               print(f"{current_loot} equipped")
                  #              print(f"Equipped items: {attacker.equipped}")
                   #         elif isinstance (current_loot, items.Armour):
                    #            if current_loot.category == "armour":
                    #                player.equipped['Armour'] = current_loot
                     #               print(f"{current_loot} equipped")
                      #              print(f"Equipped items: {attacker.equipped}")
                       #         elif current_loot.category == "shield":
                    #                player.equipped['Shield'] = current_loot
                     #               print(f"{current_loot} equipped")
                      #              print(f"Equipped items: {attacker.equipped}")
                   #         elif isinstance (current_loot, items.MagicItem):
                    #            player.equipped['Magic Item'] = current_loot
                     #           print(f"{current_loot} equipped")
                      #          print(f"Equipped items: {attacker.equipped}")
                   #         break
                    #    elif loot_choice == '3':
                     #       print(f"You leave the {current_loot.name} behind")
                      #      break
                    #    else:
                     #       print("Invalid input, please enter 1, 2 or 3. ")
                      #      continue
                 #   break

            current_room, current_enemy, current_loot = movement.direction_choice()
            print(f"You enter a {current_room.name}.")
            print(f"{current_room.description}")
            print(f"In the room you see a {current_enemy.name} and a {current_loot.name}.")
            print(f"The {current_enemy.name} attacks!")
            
            initiate_combat(player, current_enemy)

        current_turn_index = 1 - current_turn_index
    
def check_defender_state(player, defender):
    if defender == player:
        
        print(f"\n{player.name}, your quest ends here")
        stop_game()
        start_new_game(player)
        
      #  return defender
               # break

    elif defender != player:

        current_loot = defender.loot
        while True:
            if isinstance (current_loot, items.Treasure):
                if current_loot.name == "tome of the sorcerer.":
                    print("The tome contains many spells, but of particular interest is a teleportation spell you could use to leave the mansion.")
                    escape = input("Press t to teleport out of the mansion. You can also press t later if you do not wish to leave now, in which case press enter. ").lower()
                    if escape == 't':
                        print("You use the spell in the sorcerers tome to teleport yourself out of Katscurse Mansion.\nCongratulations, you have survived!")
                        return stop_game()
                      #  return
                    loot_choice = input(f"To add {current_loot.name} to inventory, press 1, to leave it here, press 3. ")
                    if loot_choice == '1':
                        player.inventory.append(current_loot)
                        print(f"{current_loot.name} added to inventory")
                    #    print(f"Inventory {player.inventory}")
                        break
                    elif loot_choice == '3':
                        print(f"You leave the {current_loot.name} behind")
                        break
                    else:
                        print("Invalid input. Please enter 1 or 3")
                        continue
            else:
                loot_choice = input(f"To add {current_loot.name} to inventory, press 1, to euip it, press 2, to leave it here, press 3. ")
                if loot_choice == '1':
                    player.inventory.append(current_loot)
                    print(f"{current_loot.name} added to inventory")
                #    print(f"Inventory {player.inventory}")
                    break
                    
                elif loot_choice == '2':
                                        
                    if isinstance (current_loot, items.Weapon):
                        player.equipped['Weapon'] = current_loot
                        player.weapon = current_loot
                        print(f"{current_loot} equipped")
                        
                   #     print(f"Equipped items: {player.equipped}")
                        break
                    elif isinstance (current_loot, items.Armour):
                        if current_loot.category == "armour":
                            player.equipped['Armour'] = current_loot
                            print(f"{current_loot} equipped")
                     #       print(f"Equipped items: {player.equipped}")
                            break
                        elif current_loot.category == "shield":
                            player.equipped['Shield'] = current_loot
                            print(f"{current_loot} equipped")
                    #        print(f"Equipped items: {player.equipped}")
                            break
                    elif isinstance (current_loot, items.MagicItem):
                        player.equipped['Magic Item'] = current_loot
                        print(f"{current_loot} equipped")
                    #    print(f"Equipped items: {player.equipped}")
                        break
                elif loot_choice == '3':
                    print(f"You leave the {current_loot.name} behind")
                    break
                else:
                    print("Invalid input, please enter 1, 2 or 3. ")
                    continue
    return defender
          #  break


def melee_attack(attacker, defender):
    print(f"{attacker.name} attacks with {attacker.weapon}.")
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.melee_bonus)
    
    print(f"{attacker.name} attack roll: {attack}")
    
    if attack > defender.get_total_protection():
        damage_dealt = attacker.weapon.damage_roll()
        defender.life -= damage_dealt
        print(f"{defender.name} takes {damage_dealt} damage")
        print(f"{defender.name} has {defender.life} life remaining")
        


def ranged_attack(attacker, defender):
    print(f"{attacker.name} attacks with {attacker.weapon}.")
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.ranged_bonus)
    print(f"{attacker.name} attack roll: {attack}")
    if attack > defender.get_total_protection():
        damage_dealt = attacker.weapon.damage_roll()
        defender.life -= damage_dealt
        print(f"{defender.name} takes {damage_dealt} damage")
        print(f"{defender.name} has {defender.life} life remaining")
        

def magic_attack(attacker, defender):
    print(f"{attacker.name} attacks with {attacker.weapon}.")
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.magic_bonus)
    print(f"{attacker.name} attack roll: {attack}")
    if attack > defender.get_total_protection():
        damage_dealt = attacker.weapon.damage_roll()
        defender.life -= damage_dealt
        print(f"{defender.name} takes {damage_dealt} damage")
        print(f"{defender.name} has {defender.life} life remaining")
        


