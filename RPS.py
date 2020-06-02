import random

choice = ['rock', 'paper','scissors']


n = 5
while n > 0:
    n -=1
    pc_choice = random.choice(choice)
    p1_choice = input('Choose Rock, Paper or Scissors:\n')
    print('The computer picked',pc_choice)
    if pc_choice == p1_choice:
        print('A tie!')
    elif pc_choice == 'rock' and p1_choice == 'paper':
        print('You win!')
    elif pc_choice == 'paper' and p1_choice == 'scissors':
        print('You win')
    elif pc_choice == 'scissors' and p1_choice == 'rock':
        print('You win!')
    elif pc_choice == 'rock' and p1_choice == 'scissors':
        print('The computer wins!\n')
    elif pc_choice == 'rock' and p1_choice == 'paper':
        print('You win!')
    elif pc_choice == 'paper' and p1_choice == 'rock':
        print('You win!')
