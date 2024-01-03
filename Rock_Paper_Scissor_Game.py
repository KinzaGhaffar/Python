Rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

Paper = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
'''

Scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

print("What would you choose? 0 for Rock, 1 for Paper or 2 for Scissors?")

game = [Rock, Paper, Scissors]

user_choice = int(input())
print(f"You chose {user_choice}")

if user_choice < 0 or user_choice >= 3:
  print("You choose an invalid number. \n You Lose!")
else:
  print(game[user_choice])

computer_choice = random.randint(0, 2)
print(f"Computer chose: {computer_choice}")
print(game[computer_choice])

if user_choice == computer_choice:
  print("It's a draw!")
elif user_choice == 0 and computer_choice == 1:
  print("You Lose!")
elif user_choice == 0 and computer_choice == 2:
  print("You Win!")
elif user_choice > computer_choice:
  print("You Win!")
elif computer_choice > user_choice:
  print("You Lose!")
