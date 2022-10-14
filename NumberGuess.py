import random

def number_picking():
    numbers = [i for i in range(1,100)]
    computer_choice = random.choice(numbers)
    return computer_choice


def guessing_game():
    print("Welcome to the number guessing game!")
    print("I'm thinking of a number between 1 and 100.")
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

    count = 10
    if difficulty == "easy":
        count = 10
    else:
        count = 5

    number = number_picking()
    while count > 0:
        print(f"You have {count} attempts remaining to guess the number.")
        guess = int(input("Make a guess: "))


        if guess == number:
            print(f"You got it the answer was: {guess}")
            print("Goodbye!")
            break

        elif guess > number:
            print("Too high")
            print("Guess again")
            count -= 1

        else:
            print("Too low")
            print("Guess again")
            count -= 1
    
    if count == 0:
        print("You lose!")



guessing_game()
    