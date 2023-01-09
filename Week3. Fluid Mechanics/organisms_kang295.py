"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 03.4 - Organisms
Date: 09/15/2022

Description:
    This program calculates the approximation of population of organisms based on user input
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

    start = float(input('Starting population, in thousands: '))  #getting the input
    inc = float(input('Average daily increase, in percent: '))
    num = int(input('Number of days to multiply: '))
    new = start

    print('Day   Approx. Pop')
    i = 0  #counting value
    print(f'{i:3}', end='')
    print(f"{new:14,.3f}")
    i = 1
    while i < num + 1:  #loop that goes to number of days
        
        new = new * (inc / 100) + new  #calculation of population updated
        new = float(new)
        print(f'{i:3}', end='')
        if i < 10: #when number is below 10
            print(f"{new:14,.3f}")
        elif i <= 99:  #when number is below 100
            print(f"{new:14,.3f}")
        else:  #when number is above or equal to 100
            print(f"{new:14,.3f}")
        i += 1

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
