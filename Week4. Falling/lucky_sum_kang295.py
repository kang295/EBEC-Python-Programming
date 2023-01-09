"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 04.2 - Lucky Sum
Date: 09/30/2022

Description:
    This program calculates the sum between two inputs which are not divisible by 3 and outputs the sum.
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
def lucky_sum(a, b):  #sum function between two given numbers 
    if a < b:
        total = 0
        bet_list = list(range(a,b+1))  #make a list of array between two given numbers
        for i in range(len(bet_list)): #this loop only adds numbers which are not divisible by 3
            if bet_list[i] % 3 != 0:
                total += bet_list[i]
    else:
        total = 0
        bet_list = list(range(b,a+1))  #make a list of array between two given numbers
        for i in range(len(bet_list)): #this loop only adds numbers which are not divisible by 3
            if bet_list[i] % 3 != 0:
                total += bet_list[i]
    return total  #returning the output value

def main():
    first = int(input('Enter the first integer: '))  #first input
    second = int(input('Enter the second integer: '))  #second input
    lucky = lucky_sum(first,second)
    print(f'The sum of the lucky numbers is {(lucky):,}.')



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
