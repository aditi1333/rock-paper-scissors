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

#Write your code below this line 👇
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
if user_choice == 0:
  print("You choose rock", (rock))
elif user_choice == 1:
  print("You choose paper",(paper))
elif user_choice == 2:
  print("You choose scissors",(scissors))
else:
  print("Choose between 0,1,2")
  
#choice by computer  
import random
available_choices = [0, 1, 2]
computer_choice = (random.choice(available_choices))
if computer_choice == 0:
  print("computer choose rock", (rock))
elif computer_choice == 1:
  print("computer choose paper",(paper))
elif computer_choice == 2:
  print("computer choose scissors",(scissors))

#finding out user win or loose

if computer_choice == user_choice:
    print("draw")
elif computer_choice == 0 and user_choice == 1:
    print("You Win!")
elif computer_choice == 1 and user_choice == 2:
    print("You Win!")           
elif computer_choice == 2 and user_choice == 3:
    print("You Win!")
else:
    print("You Loose")              
                    
          
















  
