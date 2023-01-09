"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 10.4 - Sin Cos
Date: 11/10/2022

Description:
    This program draw a plot of sine and cosine from 0 to 2π on the same axes.

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
from matplotlib import pyplot as plt
import numpy as np
"""Write new functions below this line (starting with unit 4)."""

def main():
    value = np.pi #defining pi using numpy
    fig, ax = plt.subplots() #initializing plot
    xrange = np.arange(0, (2*value), 0.01) #setting x range
    b = np.sin(xrange) #sin graph
    c = np.cos(xrange) #cos graph

    ax.plot(xrange, b, color='red')
    ax.plot(xrange, c, color='blue')

    for spine in ['top', 'right']:  #plot axis formatting
        ax.spines[spine].set_visible(False)
    for spine in ['bottom', 'left']:
        ax.spines[spine].set_position('zero')

    ax.set_xticks([(value/2), value, (3*value/2), 2*value])
    ax.set_xticklabels(['$\\pi/2$', '$\\pi$', '$3\\pi/2$', '$2\\pi$']) #expression with pi 
    ax.set_yticks([-1,1])    

    plt.show()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
