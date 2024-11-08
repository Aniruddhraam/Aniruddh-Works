import random

def game():
    number_to_guess = random.randint(1, 100)
    guess = None
    attempts = 0

    while guess != number_to_guess:
        guess = input("Guess a number between 1 and 100: ")
        attempts += 1

        if not guess.isnumeric():
            print("Please enter a number.")
            continue

        guess = int(guess)

        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")

    print(f"Congratulations! You found the number in {attempts} attempts.")

def main():
    while True:
        game()
        play_again = input("Do you want to play again? (yes/no) ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()
