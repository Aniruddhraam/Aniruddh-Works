import random

def game():
    while True:
        choices = {"R": "rock", "P": "paper", "S": "scissors"}
        computer_choice = random.choice(list(choices.values()))
        player_choice = input("Enter your choice (R, P, S, or 'Q'): ").upper()

        if player_choice == 'Q':
            break

        try:
            player_choice = choices[player_choice]
        except KeyError:
            print("Invalid choice. Please choose R, P, S or 'Q'.")
            continue

        print("Computer chose:", computer_choice)
        print("It's a tie!" if player_choice == computer_choice else "You win!" if (player_choice, computer_choice) in 
             (("rock", "scissors"), ("scissors", "paper"), ("paper", "rock")) else "You lose!")

game()
