"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 10.2 - Gas Prices
Date: 11/09/2022

Description:
    This program eads the contents of the txt file, and uses matplotlib to plot the
data as a line graph

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
"""Write new functions below this line (starting with unit 4)."""

def main():
    data_into_list = []
    with open("2008_Weekly_Gas_Averages.txt") as file:  #open the file and store the element of each line to the list
        for line in file:
            data_into_list.append(float(line.rstrip()))

    fig, ax = plt.subplots() #plot initialization 
    ax.set_xticks([10, 20, 30, 40, 50])
    ax.set_title("2008 Weekly Gas Prices") #plot title
    ax.set_xlabel("Weeks (by number)") #plot labeling by axis
    ax.set_ylabel("Average Price (dollars/gallon)")
    ax.set_xlim(1,52) #setting the limit of each axis
    ax.set_ylim(1.5, 4.25)
    ax.grid() #generating a grid line
    ax.plot(range(1,53), data_into_list) #storing plot information
    plt.show()
    file.close()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
