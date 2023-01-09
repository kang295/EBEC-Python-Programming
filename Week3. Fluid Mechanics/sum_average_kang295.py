"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 03.2 - Sum Average
Date: 09/15/2022

Description:
    This program is getting the input which is greater than 0 and calculates the average and sum.
    When negative value is inputted, the process stops

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

    num = float(input('Enter a non-negative number (negative to quit): ')) #getting the input
    sum = 0  #initiallizing
    cnt = 0
    
    if num >= 0:       #when value is greater than 0
        while num >= 0:   #checking if value is greater than 0
            sum = sum+num  #updating the sum
            num = float(input('Enter a non-negative number (negative to quit): '))
            cnt = cnt+1  #updating the number of count
            
        print(f'  You entered {(cnt)} numbers.')
        avg = sum / cnt #average calculation
        sum = format(sum, ".3f")
        avg = format(avg, ".3f")
        print(f'  Their sum is {(sum)} and their average is {(avg)}.')
    else:
        print('  You didn\'t enter any numbers.')
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
