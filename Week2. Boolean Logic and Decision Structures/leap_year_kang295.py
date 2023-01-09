"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 02.1 - Leap Year
Date: 09/07/2022

Description:
    This program inputs the year user wants and calculates how many days are in that February
    

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
    year = int(input('Enter a year: ')) #printing what year the user wants to know
    
    if ((year % 400) == 0): #checking leap year
        print(f'The year {(year)} is a leap year.') #printing
        print(f'February of {(year)} has 29 days.') #printing
    elif (year % 100) == 0: #checking leap year
        print(f'The year {(year)} is not a leap year.') #printing
        print(f'February of {(year)} has 28 days.') #printing
    elif (year % 4) == 0:  #checking leap year
        print(f'The year {(year)} is a leap year.') #printing
        print(f'February of {(year)} has 29 days.') #printing
    else:  #checking leap year
        print(f'The year {(year)} is not a leap year.') #printing
        print(f'February of {(year)} has 28 days.') #printing


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
