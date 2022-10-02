"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 01.2 - Interest
Date: 08/30/2022

Description:
    This program is calculating the banking interest and outputs the future value based on the original deposited money and annual interest rate

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

    print('Enter the following parameters.') #getting the input needed
    init = int(input('  ' + 'The initial deposit? ')) #getting the originally deposited amount
    int_rate = float(input('  ' + 'The annual interest rate in percent? ')) #annual interest rate
    rate = int_rate / 100 #should be in a form of percentage
    years = float(input('  ' + 'The number of years the account earn interest? ')) #number of years earning interest
    times = int(input('  ' + 'The number of times interest is compounded each year: ')) #compounded number of times
    future_value = init*(1+(rate/times))**(times*years) #calculating future value
    value = "${:,.2f}".format(future_value) #future value is expressed as dollars currency
    print('The balance of this account will be', format(value) + f' after {float(years)} years.') #printing the output
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
