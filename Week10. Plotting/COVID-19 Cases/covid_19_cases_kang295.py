"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 10.3 - Covid 19 Cases
Date: 11/10/2022

Description:
    This program write a program that reads the contents of the file and calculates the total number of cases
    for each week by summing all of the new cases prior to and including that week.Then, create a bar chart plotting
    the total cases for each week versus the week’s start
date
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
import datetime
"""Write new functions below this line (starting with unit 4)."""

def main():
    total = []
    sum = 0

    f=open('indiana_covid-19_data_fall_2022.txt', "r") #file opening and store the specific column value in a list
    lines=f.readlines()
    col1 = []
    col3 = []
    for x in lines:
        col1.append(x.split(' ')[0])
    for x in lines:
        col3.append(x.split(' ')[2])

    for i in range(len(col3)): #calculating total sum of new cases
        sum += float(col3[i])
        total.append(int(sum)/1000)
    
    #plot generation part
    fig, ax = plt.subplots() #plot initialization 
    x = []
    for date in col1: #getting datetime object with year, month, and day
        y, m, d = date.split('-') 
        dt = datetime.date(int(y), int(m), int(d))
        x.append(dt)
    ax.bar(x, total, width = 7) #storing plot information
    #fig.autofmt_xdate()

    ax.set_title("Weekly Positive COVID-19 Cases in Indiana") #plot title
    ax.set_xlabel("Date") #plot labeling by axis
    ax.set_ylabel("Number of Cases (in thousands)")
    ax.set_ylim(0, 2100)
    
    plt.show()
    f.close()
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
