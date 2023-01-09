"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 04.1 - Falling
Date: 09/28/2022

Description:
    This program calculates the distance based on the gravitational force and time
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
    
    print('Time (s)  Distance (m)')
    print('----------------------')
    for i in range (51):   #this allows to get only the value of multiple of 5
        if i % 5 == 0 and i > 0:
            distance = falling_dist(i)
            print(" %7d %13.1f" % (i, distance))  #printing with adjusted format

def falling_dist(i):  #distance calculator
    grav = 8.87
    distance = 0.5*grav*(i**2)  #formula for calculating distance
    
    return distance


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
