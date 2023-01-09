"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 10.1 - Monthly Sales
Date: 11/09/2022

Description:
    This program collects monthly sales data from the user and
    stores it in a list.

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
    month_list = ['January', 'February', 'March', 'April', 'May', 'June', 
    'July', 'August', 'September', 'October', 'November', 'December']  #month list
    num_list = []
    
    for i in range(12): #storing input into the new list
        value = int(input(f'Enter the sales for {(month_list[i])}: '))
        num_list.append(value)

    mycolors = ['#4D4038', '#BAA892','#5B6870','#6E99B4', '#A3D6D7', '#085C11', '#849E2A',
    '#C3BE0B','#E9E45B','#6B4536','#B46012','#FF9B1A']  #list for different colors

    y = np.array(num_list) #creating an array
    plt.pie(y, labels = month_list, colors = mycolors) #generating a pie chart
    plt.title(label = "Monthly Sales Values") #title
    plt.show() #command for showing a complete pie chart 

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
