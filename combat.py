from dice import roll_dice
from main import main

def is_alive(self):
    return self.life > 0

def roll_initiative(player, enemy):
    player_initiative = roll_d20()
    enemy_initiative = roll_d20()
    if player_initiative > enemy_initiative:
        return [player, enemy]
    elif enemy_initiative > player_initiative:
        return [enemy, player]
    else:
        roll_initiative(player, enemy)


def start_battle(turn_order):
    first, second = turn_order
    current_turn_index = 0
    participants = [first, second]
    while first.is_alive() and second.is_alive():
        attacker = participants[current_turn_index]
        defender = participants[1 - current_turn_index]
        weapon_category = attacker.weapon.category
        if attacker.is_alive():
            if weapon_category == "melee":
                melee_attack(attaker, defender)
            elif weapon_category == "ranged":
                ranged_attack(attaker, defender)
            elif weapon_category =="magic":
                magic_attack(attaker, defender)
        if not defender.is_alive():
            print(f"\n{defender.name} has been defeated!")
            if defender = player:
                print(f"\n{player.name}, your quest ends here")
                game_running = false
            break

        current_turn_index = 1 - current_turn_index


def melee_attack(first, second):




def ranged_attack(first, second):




def magic_attack(first, second):