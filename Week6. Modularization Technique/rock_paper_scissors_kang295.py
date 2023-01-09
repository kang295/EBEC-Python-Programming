"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 06.2 - Rock Paper Scissors
Date: 10/21/2022

Description:
    This program generates two digit random number and three digit random number and ask
    the user to put the correct answer. 
    

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""
import random

def main():
    first = get_computer_choice()
    second = get_player_choice()
    a = get_winner(first, second)
    while a == 'tie':    #case when the result is tie
        print('')
        first = get_computer_choice()
        second = get_player_choice()
        a = get_winner(first, second)

def get_computer_choice(): #returns a value as a string either 'rock', 'Scissors', 'paper'
    choice_list = ['rock', 'paper', 'scissors']  #assigning the list of choice
    comp = random.choice(choice_list)
    return comp

def get_player_choice():  #returns a value as a string either 'rock', 'Scissors', 'paper'
    choice_list = ['rock', 'paper', 'scissors']
    user = input('Choose rock, paper, or scissors: ')
    while user not in choice_list:  #reiterating if wrong selection is made
        print('You made an invalid choice. Please try again.')
        user = input('Choose rock, paper, or scissors: ')
    return user
    
def get_winner(first, second): #defining who is the winner
    if first == second:
        print(f'  The computer chose {first}, and you chose {second}.')
        print('  It\'s a tie. Starting over.')
        return 'tie'
    elif first == 'rock':
        if second == 'scissors':
            print(f'  The computer chose {first}, and you chose {second}.')
            print('  rock beats scissors')
            print('  You lost.  Better luck next time.')
            print('Thanks for playing.')
            return 'computer'
        else:
            print(f'  The computer chose {first}, and you chose {second}.')
            print('  paper beats rock')
            print('  You won the game!')
            print('Thanks for playing.')
            return 'player'
    elif first == 'scissors':
        if second == 'rock':
            print(f'  The computer chose {first}, and you chose {second}.')
            print('  rock beats scissors')
            print('  You won the game!')
            print('Thanks for playing.')
            return 'player'
        else:
            print(f'  The computer chose {first}, and you chose {second}.')
            print('  scissors beats paper')
            print('  You lost.  Better luck next time.')
            print('Thanks for playing.')
            return 'computer'
    elif first == 'paper':
        if second == 'rock':
            print(f'  The computer chose {first}, and you chose {second}.')
            print('  paper beats rock')
            print('  You lost.  Better luck next time.')
            print('Thanks for playing.')
            return 'computer'
        else:
            print(f'  The computer chose {first}, and you chose {second}.')
            print('  scissors beats paper')
            print('  You won the game!')
            print('Thanks for playing.')
            return 'player'

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
