from dice import roll_dice
from main import main
import characters


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

        current_turn_index = 1 - current_turn_index


def melee_attack(attacker, defender):
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.melee_bonus)
    print(f"{attacker} rolls {attack}")
    if attack > defender.protection:
        damage_dealt = attacker.weapon.damage
        defender.life -= damage_dealt
        print(f"{defender} takes {damage_dealt} damage")
        print(f"{defender} has {defender.life} life remaining")




def ranged_attack(attacker, defender):
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.ranged_bonus)
    print(f"{attacker} rolls {attack}")
    if attack > defender.protection:
        damage_dealt = attacker.weapon.damage
        defender.life -= damage_dealt
        print(f"{defender} takes {damage_dealt} damage")
        print(f"{defender} has {defender.life} life remaining")

def magic_attack(attacker, defender):
    attack = roll_dice(20) + (attacker.weapon.bonus + attacker.magic_bonus)
    print(f"{attacker} rolls {attack}")
    if attack > defender.protection:
        damage_dealt = attacker.weapon.damage
        defender.life -= damage_dealt
        print(f"{defender} takes {damage_dealt} damage")
        print(f"{defender} has {defender.life} life remaining")

def initiate_combat(player, enemy):
    turn_order = roll_initiative(player, enemy)
    start_battle(turn_order, player)
