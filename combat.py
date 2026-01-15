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
        elif weapon_category == "magic weapon":
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
       

    current_loot = defender.loot
    if not current_loot:
        print(f"{defender.name} had nothing of value.")
        return True
    while True:
        if isinstance (current_loot, items.Treasure) and current_loot.name == "tome of the sorcerer.":
           
            print("The tome contains many spells, but of particular interest is a teleportation spell you could use to leave the mansion.")
            print("Add the tome to your inventory, then Press t to teleport out of the mansion when you are not in combat.")
          

        print(f"\nYou found {current_loot.name}")
        damage_info = f"Damage: {current_loot.dice}" if hasattr(current_loot, "dice") and current_loot.damage_roll is not None else ""
        protection_info = f"Protection: {current_loot.protection}" if hasattr(current_loot, "protection") and current_loot.protection is not None else ""
        value_info = f"Value: {current_loot.value}" if hasattr(current_loot, "value") and current_loot.value is not None else ""
        life_info = f"Life: {current_loot.life}" if hasattr(current_loot, "life") and current_loot.life is not None else ""
        details = ", ".join(filter(None, [damage_info, protection_info, value_info, life_info]))
        print(f"Properties: {details}")

        print(f"Currently equipped items:\nWeapon: {player.weapon}\nArmour: {player.equipped_armour}\nShield: {player.equipped_shield}\nMagic: {player.equipped_magic}")
        loot_choice = input(f"To add {current_loot.name} to inventory, press 1, to equip it, press 2, to leave it here, press 3. ")
        
        if loot_choice == '1':
            player.inventory.append(current_loot)
            print(f"{current_loot.name} added to inventory")
                    
            break
        elif loot_choice == '2':
            if isinstance(current_loot, items.Weapon):
                player.weapon = current_loot
                player.equipped['Weapon'] = current_loot
                print(f"{current_loot.name} equipped.")
            elif isinstance(current_loot, items.Armour):
                if current_loot.category == "armour":
                    player.equipped_armour = current_loot
                    player.equipped['Armour'] = current_loot
                    print(f"{current_loot.name} equipped.")
                elif current_loot.category == "shield":
                    if player.weapon.hands == 1:
                        player.equipped_shield = current_loot
                        player.equipped['Shield'] = current_loot
                        print(f"{current_loot.name} equipped.")
                    else:
                        player.inventory.append(current_loot)
                        print("You cannot equip a shield as you are using a 2 handed weapon. Shield has been added to inventory.")
            elif isinstance(current_loot, items.MagicItem):
                player.equipped_magic = current_loot
                player.equipped['Magic Item'] = current_loot
                print(f"{current_loot.name} equipped")
                break
            elif isinstance(current_loot, items.Treasure):
                player.inventory.append(current_loot)
                print(f"{current_loot.name} cannot be equipped. It has been added to inventory")
                break
        
            break
        elif loot_choice == '3':
            print(f"You leave the {current_loot.name} behind")
            break
        else:
            print("Invalid input. Please enter 1, 2 or 3")
                      
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
        


