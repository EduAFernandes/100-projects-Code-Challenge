import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


images = [rock, paper, scissors]

player_choice = int(input("Type 0 for rock, 1 for paper or 2 for scissors.\n"))
if player_choice >= 3 or player_choice < 0:
    print("you typed an invalid number, you lose!")
else:
    print("You chose", images[player_choice])
    machine_choice = random.randint(0, 2)
    print("Computer chose: ")
    print(images[machine_choice])



    if player_choice == 0 and machine_choice == 2:
        print("You win")
    elif player_choice == 2 and machine_choice == 0:
        print("You lose")
    elif player_choice < machine_choice:
        print("You Lose")
    elif machine_choice < player_choice:
        print("You Win")
    elif player_choice == machine_choice:
        print("It's a draw")
