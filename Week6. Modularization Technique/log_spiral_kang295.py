"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 06.4 - Log Spiral
Date: 10/21/2022

Description:
    This program draws a spiral shape by using given equations and math module

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
from turtle import *
from math import *

"""Write new functions below this line (starting with unit 4)."""


def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(564, 564)
    width(5)


def main():
    """Write your mainline logic below this line (then delete this line)."""
    penup()
    for i in range(1081): # for loop iterates to meet the given spiral image
        theta = radians(i) # theta is calculated in radians
        x = 4 * exp(0.22*theta)*cos(theta)  #given x equation
        y = 4 * exp(0.22*theta)*sin(theta)  #given y equation
        goto(x,y)
        pendown()
        i += 5 #angle update
    goto(x,y)  #shortest linear path between two location(x and y)


"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
