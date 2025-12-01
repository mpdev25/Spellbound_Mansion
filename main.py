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
    
def intro():
    print("In the warm, cozy confines of the Drunken Demigorgan Tavern, the only watering hole in Snagleback village, you contemplate the choices that led you here and the future that awaits.")


def main():
    game_running = True
    while game_running:
        game_state = intro() 
        game_running = start_new_game()



if __name__ == "__main__":
    main()