from dice import roll_dice
import characters
import items 

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

    print("I couldn't help but hear you talking of a mysterious mansion nearby")
    print("The old Katscurse mansion, it's just a mile North of here, but I wouldn't go there if I was you the man says as his companions nod.")
    print("It belonged to the sorcerer, Paskratos, but he hasn't been seen for fifty years. Some unwise people have enterd the mansion over the years in search of riches, but none has ever been seen again.")
    print("The man looks at you thoughtfully for a moment, studying the keen interest in the mansion that the look on your face betrays.")
    print("Finally he lets out a sigh and exclaims \"I can see you are an unwise person. At least wait till the morning and I will give you my old fathers leather armour. I doubt it will help much, but better than nothing perhaps.\"")
    print(".......")
    print("The next morning you collect the leather armour and head out to Katscurse mansion, a spring in your step adn a smile on your face -- treasue awaits!")
    


    


def main():
    game_running = True
    while game_running:
        game_state = intro() 
        game_running = start_new_game()



if __name__ == "__main__":
    main()