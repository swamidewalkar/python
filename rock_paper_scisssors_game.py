
import random


def get_choices():
    player_choice = input("enter your choice(rock,paper,scissors):")
    available_choices = ["rock","paper","scissors"]
    computer_choice = random.choice(available_choices)
    selected_choice = {"player":(player_choice),"computer":(computer_choice)}

    return selected_choice 




def get_win (player,computer) :
    print(f"you chose {player} and computer chose {computer}")
    if player==computer :
        return "it is a tie ! "
    elif player == "rock" and computer == "paper":
        return "you lose :("
    elif player=="rock" and computer=="scissors" :
        return "you won"
    
    elif player == "paper" and computer == "scissors":
        return "you lose :("
    elif player=="paper" and computer=="rock" :
        return "you won"

    elif player == "scissors" and computer == "rock":
        return "you lose :("
    elif player=="scissors" and computer=="paper" :
        return "you won"

choices = get_choices()

result = get_win(choices["player"],choices["computer"] )
print(result)


