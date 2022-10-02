"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 02.5 - Fluid Mechanics
Date: 09/11/2022

Description:
    This program calculates the Reynolds number with given inputs
    

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

    temp = float(input('Enter the temperature in °C as 5, 20, or 50: ')) #getting input and store the value

    if temp == 5:  #when diferent temp is received
        kin_vis = 1.52*10**(-6) 
    elif temp == 20:
        kin_vis = 1.00*10**(-6)
    elif temp == 50: 
        kin_vis = 5.54*10**(-7)

    velocity = float(input('Enter the velocity of water in the pipe (m/s): '))
    diameter = float(input('Enter the pipe\'s diameter (m): '))

    Re = (velocity)*(diameter) / kin_vis  #calcualtion for Reynolds number
    Re = '{:.2e}'.format(Re)
    print(f'At {temp}\u00B0C, the Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe is {Re}.') 


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
