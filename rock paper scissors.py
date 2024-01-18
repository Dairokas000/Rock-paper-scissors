Playerchoice = input("What do you play")
Player2choice = input("What do you play")


if Playerchoice == "rock" and Player2choice == "paper":
    print("Player 2 wins")
elif Playerchoice == "rock" and Player2choice == "scissors":
    print("Player 1 wins")
elif Playerchoice == "rock" and Player2choice == "rock":
    print("tie")
elif Playerchoice == "paper" and Player2choice == "rock":
    print("player 1 wins")
elif Playerchoice == "paper" and Player2choice == "scissors":
    print("Player 2 wins")
elif Playerchoice == "paper" and Player2choice == "paper":
    print("tie")
elif Playerchoice == "scissors" and Player2choice == "rock":
    print("Player 2 wins")
elif Playerchoice == "scissors" and Player2choice == "paper":
    print("Player 1 wins")
elif Playerchoice == "scissors" and Player2choice == "scissors":
    print("tie")
