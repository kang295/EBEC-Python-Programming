"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 07.2 - Number Analysis
Date: 10/23/2022

Description:
    This program gets 10 floating inputs from the user and calculates the 
    highest, lowest, total and average value.

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
import math 

"""Write new functions below this line (starting with unit 4)."""

def get_number_list():  #function for getting the list element inputs
    list = []
    for i in range(10):  #iterating 10 times to get 10 inputs
        if i < 9:
            element = input(f'  number  {i+1} of 10: ')
        else:
            element = input(f'  number {i+1} of 10: ')
        list.append(float(element))  #appending inputs to a new list
    return list

def main():
    print('Enter 10 numbers:')
    get = get_number_list()
    high = "{:.2f}".format(max(get))  #formatting with 2 decimals
    low = "{:.2f}".format(min(get))
    total = "{:.2f}".format(sum(get))
    avg = "{:.2f}".format(sum(get)/len(get))

    print(f'Highest number: {high}')
    print(f'Lowest number: {low}')
    print(f'Total: {total}')
    print(f'Average: {avg}')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
