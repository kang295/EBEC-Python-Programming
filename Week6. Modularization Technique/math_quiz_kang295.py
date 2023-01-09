"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 06.1 - Math Quiz
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
from random import randint, randrange

def main():
    a = random_number(2)  #storing 2 digit random number
    b = random_number(3)  #storing 3 digit random number
    sum = int(calc(a,b))  #storing calculated sum
    print(f'   {a}')
    print(f'+ {b}')
    print('-----')
    val = int(input('= '))  #storing the input number
    if sum != val:   #comparing statement
        print(f'Incorrect. The correct answer is {sum}.')
    else:
        print('Correct -- Good Work!')

def random_number(spec):   #random number generator
    range_start = 10**(spec-1)
    range_end = (10**spec)-1
    return randint(range_start, range_end)

def calc(a,b):   #calculation
    c = a + b
    return c
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
