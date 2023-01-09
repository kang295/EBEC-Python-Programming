"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 07.4 - Magic Square
Date: 10/24/2022

Description:
    This program gets 2 dimentional list and check if the matrix is a Lo Shu Magic Square.

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
import math 
import random

"""Write new functions below this line (starting with unit 4)."""

def print_square(a): #printing 2 dimentional list
    for i in range (3):
        print('  ', end='')
        for j in range(3):
            num = a[i][j]
            if j < 2:
                print(f'{num} ', end='')
            else:
                print(f'{num}')

def is_magic(a):  #checking if it is lo shu magic square, using boolean
    deter = True
    if(a[0][0] + a[0][1] + a[0][2] != 15 or a[1][0] + a[1][1] + a[1][2] != 15 or a[2][0] + a[2][1] + a[2][2] != 15): #row sum
        deter = False
    if(a[0][0] + a[1][0] + a[2][0] != 15 or a[0][1] + a[1][1] + a[2][1] != 15 or a[0][2] + a[1][2] + a[2][2] != 15): #column sum
        deter = False
    if(a[0][0] + a[1][1] + a[2][2] != 15 or a[0][2] + a[1][1] + a[2][0] != 15): #diagonal sum
        deter = False
    else:  #repating case with number 5
        cnt = 0
        for i in range(3):  #checking if there is case when 5 is used more than once
            for j in range(3):
                if a[i][j] == 5:
                    cnt += 1
        if cnt > 1:
            deter = False
    return deter

def main():
    first = [[1, 2, 3], [4, 5, 6], [7, 8, 9]] #first example case
    second = [[5, 5, 5], [5, 5, 5], [5, 5, 5]] #second example case
    third = [[4, 9, 2], [3, 5, 7], [8, 1, 6]] #third example case

    print('Your square is:')
    print_square(first)
    if(is_magic(first) == True):  #boolean check and print the statement
        print('It is a Lo Shu magic square!')
        print('')
    else:
        print('It is not a Lo Shu magic square.')
        print('')
    
        print('Your square is:')
    print_square(second)
    if(is_magic(second) == True):  #boolean check and print the statement
        print('It is a Lo Shu magic square!')
        print('')
    else:
        print('It is not a Lo Shu magic square.')
        print('')

    print('Your square is:')
    print_square(third)
    if(is_magic(third) == True):  #boolean check and print the statement
        print('It is a Lo Shu magic square!')
        print('')
    else:
        print('It is not a Lo Shu magic square.')
        print('')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
