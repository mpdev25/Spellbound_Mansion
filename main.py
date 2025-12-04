import tkinter as tk



def start_new_game():
    while True:
        user_input = input("Start a new game? y/n ").lower()
        if user_input == "y":
            return True
        if user_input == "n":
            return False
        else:
            print("Invalid input, please enter y or n.")

def get_player_name():
    player_name = input("type name ")
    return player_name
    
def intro():
    print("In the warm, cozy confines of the Drunken Demigorgan Tavern, the only watering hole in Snagleback village, you contemplate the choices that led you here and the future that awaits.")
    print("Before leaving your village you spent a year training in secret to prepare for a life of adventure and, you hope, riches!")
    print("You focused your training on")
    print("1 Melee combat")
    print("2 Ranged combat")
    print("3 magic combat")
    try:
        choice = int(input("Enter your choice: 1, 2 or 3"))
        if choice == 1:
            print("You've become adept with the short sword your adventuress aunt left you when she died.")
        if choice == 2:
            print("You've become adept with the shortbow your adventuress aunt left you when she died")
        if choice == 3:
            print("You've become adept with the magic staff your adventuress aunt left you when she died")
        else:
            print("Invalild choice. Please enter 1, 2 or 3")
    except ValueError:
        print("Invalid input! Please enter 1, 2 or 3")
    print("As you sit finishing your ale and contemplating your next move you overhear some interesting conversation concerning an abandoned mansion not far from Snagleback village.")
    print("You turn to the people talking at the table next to you and introduce yourself.")
    print("Hi, I couldn't help but hear you talking of a mysterious mansion nearby")
    print("\"Your new here, what's your name?\" says a man whose clothing reminds you all too much of your own impoverished upbringing")
    player_name = get_player_name()
    print(f"I'm {player_name}")

    


def main():
    game_running = True
    while game_running:
        game_state = intro() 
        game_running = start_new_game()



if __name__ == "__main__":
    main()