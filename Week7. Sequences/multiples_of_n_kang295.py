"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 07.1 - Multiples of N
Date: 10/23/2022

Description:
    This program gets two inputs, integer and list as an argument. Then
    the printed list should show the lists with element that is multiple of given integer.

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

def multiples_of(a, b):
    new = []  #assigning new list
    for i in range(len(b)):  #check if elements in the list is multiples of 13
        if (b[i] % a) == 0:  
            new.append(b[i])  #appending the element to the new list
    return new  

def main():
    first = 13   #assigning integer argument
    second = [19, 1599, -546, 10, 39, -58, 1, 85, 201, -91, 286, 799, 406]  #assigning list argument
    print('Original list of numbers:')
    print('  ', end = '')
    print(second)
    print('Numbers in the list that are multiples of 13:')
    print('  ', end = '')
    print(multiples_of(first, second))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
