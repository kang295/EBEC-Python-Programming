"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 03.1 - Cakes
Date: 08/28/2022

Description:
    This program is getting the number and it will determine the leverl of a cake

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


def main():

    num = int(input('Enter the number of layers: '))
    cnt=1  #counting parameter
    space = num
    for i in range(num):  #outer loop
        space = space-1
        
        for i in range(space): #loop for space
            print(' ', end='')
        print('[', end='')  #printing opening bracket
        for i in range(cnt):  #loop for printing star
            print('*', end ='')
        cnt= cnt+2
        print(']')  #printing closing bracket

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
