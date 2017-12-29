def game():
    print("You are about to begin a Rock, scissor and paper game!  \
    Put the name of the players above")

    player_1 = input("What's is your name?")
    player_2 = input("What's is the name of the second player?")

    play_1 = input(player_1+" choose rock, scissor or paper:")
    play_2 = input(player_2+" choose rock, scissor or paper:")

    def winner():
        rock = "rock"
        paper = "paper"
        scissor = "scissor"
        if (rock and paper):
            print("Paper wins!")
            if (player_1 is rock and player_2 is paper):
                print(player_2+" won the game!Congrats!!!")
            else:
                print(player_1+" won the game!Congrats!!!")
        elif (rock and scissor):
            print("Rock wins!")
            if (player_1 is rock and player_2 is scissor):
                print(player_1+" won the game!Congrats!!!")
            else:
                print(player_2+" won the game!Congrats!!!")
        else:
            print("Scissor wins")
            if (player_1 is scissor and player_2 is paper):
                print(player_1+" won the game!Congrats!!!")
            else:
                print(player_2+" won the game!Congrats!!!")

    while (play_1 == play_2):
        print("Oops! Play again!")
        play_1 = input(player_1+" choose rock, scissor or paper:")
        play_2 = input(player_2+" choose rock, scissor or paper:")
        break
    else:
        print(player_1+" and "+player_2+" typed "+play_1+" and "+play_2)
        winner()

game()
