"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 04.4 - Prime Numbers
Date: 10/03/2022

Description:
    This program gets an input value and determines if it is prime number or not. If also terminates the program
    if -1 is entered

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
from math import sqrt

"""Write new functions below this line (starting with unit 4)."""

def is_prime(value): #prime number function that determines if it is prime or not
    pr = False
    if value == 2:
        pr = True  #2 is a prime number
    if value > 2:
        pr = True
        for i in range(2, int(sqrt(value))+1):  #this allows te function goes through all number except for 1 and itself
            if (value % i) == 0:
                pr = False
                break
    return bool(pr) #returning boolean expression

def main():
    check = 0
    while check != -1:  #iterate until the input is -1
        value = int(input('Enter a positive integer (-1 to quit): '))
        check = value
        if value == -1:  #exit the function when value is -1
            return

        if is_prime(value):
            print(f'  {value} is prime!')
        else:
            print(f'  {value} is not prime.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
