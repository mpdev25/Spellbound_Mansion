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
            
            return

        current_turn_index = 1 - current_turn_index
   
    
def check_defender_state(player, defender):
    if defender == player:
        
        print(f"\n{player.name}, your quest ends here")
        return False
       # stop_game()
        #start_new_game(player)
        
      #  return defender
               # break

    #elif defender != player:

    current_loot = defender.loot
    if not current_loot:
        print(f"{defender.name} had nothing of value.")
        return True
    while True:
        if isinstance (current_loot, items.Treasure) and current_loot.name == "tome of the sorcerer.":
              #  if current_loot.name == "tome of the sorcerer.":
            print("The tome contains many spells, but of particular interest is a teleportation spell you could use to leave the mansion.")
            escape = input("Press t to teleport out of the mansion. You can also press t later if you do not wish to leave now, in which case press enter. ").lower()
            if escape == 't':
                print("You use the spell in the sorcerers tome to teleport yourself out of Katscurse Mansion.\nCongratulations, you have survived!")
                stop_game()
                return False
            break
        print(f"\nYou found {current_loot.name}")
        loot_choice = input(f"To add {current_loot.name} to inventory, press 1, to equip it, press 2, to leave it here, press 3. ")
        if loot_choice == '1':
            player.inventory.append(current_loot)
            print(f"{current_loot.name} added to inventory")
                    
            break
        elif loot_choice == '2':
            if isinstance(current_loot, items.Weapon):
                player.Weapon = current_loot
                player.equipped['Weapon'] = current_loot
            elif isinstance(current_loot, items.Armour):
                if current_loot.category == "armour":
                    player.equipped_armour = current_loot
                    player.equipped['Armour'] = current_loot
                elif current_loot.category == "shield":
                    player.equipped_shield = current_loot
                    player.equipped['Shield'] = current_loot
            elif isinstance(current_loot, items.MagicItem):
                player.equipped_magic = current_loot
                player.equipped['Magic Item'] = current_loot
                print(f"{current_loot.name} equipped")
                break
            elif isinstance(current_loot, items.Treasure):
                player.inventory.append(current_loot)
                print(f"{current_loot.name} cannot be equipped. It has been added to inventory")
                break
            print(f"{current_loot.name} equipped.")
            break
        elif loot_choice == '3':
            print(f"You leave the {current_loot.name} behind")
            break
        else:
            print("Invalid input. Please enter 1, 2 or 3")
                      #  continue
    return True
         
              


def melee_attack(attacker, defender):
    print(f"{attacker.name} attacks with {attacker.weapon}.")
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.melee_bonus)
    
    print(f"{attacker.name} attack roll: {attack}")
    
    if attack > defender.get_total_protection():
        damage_dealt = attacker.weapon.damage_roll()
        
        defender.life -= damage_dealt
        current_life = defender.get_total_life()
        print(f"{defender.name} takes {damage_dealt} damage")
        print(f"{defender.name} has {current_life} life remaining")
        


def ranged_attack(attacker, defender):
    print(f"{attacker.name} attacks with {attacker.weapon}.")
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.ranged_bonus)
    print(f"{attacker.name} attack roll: {attack}")
    if attack > defender.get_total_protection():
        damage_dealt = attacker.weapon.damage_roll()
        
        defender.life -= damage_dealt
        current_life = defender.get_total_life()
        print(f"{defender.name} takes {damage_dealt} damage")
        print(f"{defender.name} has {current_life} life remaining")
        

def magic_attack(attacker, defender):
    print(f"{attacker.name} attacks with {attacker.weapon}.")
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.magic_bonus)
    print(f"{attacker.name} attack roll: {attack}")
    if attack > defender.get_total_protection():
        damage_dealt = attacker.weapon.damage_roll()
        
        defender.life -= damage_dealt
        current_life = defender.get_total_life()
        print(f"{defender.name} takes {damage_dealt} damage")
        print(f"{defender.name} has {current_life} life remaining")
        


