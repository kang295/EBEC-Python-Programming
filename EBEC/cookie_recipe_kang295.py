"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 01.3 - Cookie Recipe
Date: 08/30/2022

Description: 
    This program calulates how much butter, sugar and flour are needed to make desired amount of cookies
    

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

    number = int(input('How many cookies do you want to make? ')) #asking how many cookies does user need
    number2 = '{:,}'.format(number) #converting the number with thousands separation comma
    print(f'To make {str(number2)} cookies, you will need:') #printing statement
    
    butter = (1.25/48)*number #calculating the amount of butter needed
    butter = "{:10,.2f}".format(butter) #converting the number with thousands separation comma
    sugar = (1.5/48)*number #calculating the amount of sugar needed
    sugar = "{:10,.2f}".format(sugar) #converting the number with thousands separation comma
    flour = (2.5/48)*number #calculating the amount of flour needed
    flour = "{:10,.2f}".format(flour) #converting the number with thousands separation comma

    print(f'{(butter)} cups of butter\n' + f'{(sugar)} cups of sugar\n' + f'{(flour)} cups of flour') #printing statement
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
