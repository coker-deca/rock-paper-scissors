from mimetypes import init
import os
import random
from time import sleep

CPU_WINS = 'Computer wins'
PLAYER_WINS = 'Player wins'
options = ["R", "P", "S"]
options_dict = {"R": "Rocks", "P": "Paper", "S": "Scissors"}


def check_winner(player1, player2):
    if player1 == player2:
        return "Its a tie.\nLet's play again"
    elif player1 == 'R':
        if player2 == 'S':
            return CPU_WINS
        else:
            return PLAYER_WINS
    elif player1 == 'S':
        if player2 == 'P':
            return CPU_WINS
        else:
            return PLAYER_WINS
    else:
        if player2 == 'R':
            return CPU_WINS
        else:
            return PLAYER_WINS


def game():
    play = True
    comp_score = 0
    player_score = 0

    def gameplay():
        comp_choice = random.choice(options)
        player_choice = None
        os.system('cls')
        os.system('clear')
        nonlocal comp_score, player_score
        print("Computer Score: ", comp_score, "\nPlayer Score: ", player_score)

        print("Player turn. Please make a choice:")
        while player_choice not in options:
            player_choice = input(
                "Type: \nR for Rock\nP for Paper\nS for Scissors\n\n").upper()
            if player_choice not in options:
                print(
                    "You entered an invalid value.\nPlease enter a 'R', 'P' or 'S' only.")
            sleep(2)

        print("\nCPU: ", options_dict[comp_choice], ";\nPlayer: ", options_dict[player_choice], ";")
        winner = check_winner(comp_choice, player_choice)
        if winner == CPU_WINS:
            comp_score += 1
        elif winner == PLAYER_WINS:
            player_score += 1

        print("\n", winner)
        print("Final score is: CPU - ", comp_score,
              " and player - ", player_score, "\n")

    play = True

    while play == True:
        gameplay()
        again = input(
            "Would you like to play again? \n\nType 'Y' or 'yes' to continue, and any other key to stop the game.\n"
        )
        play = end_or_continue(again, comp_score, player_score)
    print("\n\nBye")
    os.system('cls')
    os.system('clear')


def end_or_continue(again, comp_score, player_score):
    if again != "y" and again != "Y" and again != 'yes':

        os.system('cls')
        os.system('clear')
        if comp_score == player_score:
            print("It's a tie. Come back and Play soon.")
        elif comp_score > player_score:
            print(CPU_WINS, " Come back and Play soon.")
        else:
            print(PLAYER_WINS, " Come back and Play soon.")
        input("Press any key to exit...")
        return False
    return True


game()
