"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 03.3 - Rainfall
Date: 09/15/2022

Description:
    This program calculates the average rainfall over a period of years.
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
    
    yrs = int(input('Enter the number of years: ')) #getting the year input
    if yrs <= 0: #checking if given year is equal to 0
        print('Invalid input; years must be greater than 0.')
    else:
        
        num1 = 0
        cnt = 0
        std = 12
        j = 0
        months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        sum =0
        for i in range(yrs):  #looping for number of years
            print(f'  For year No. {(i+1)}')
            for j in months:
                num = float(input(f'    Enter the rainfall for {(j)}.: '))
                while num < 0:
                    print('    Invalid input; rainfall cannot be negative.')
                    num = float(input(f'    Enter the rainfall for {(j)}.: '))
                cnt = cnt + 1
                num1 = num1 + num 
        sum = num1
        
        #calculating the total amount of rainfall
        print(f'There are {(yrs*12)} months.')
        
        m_avg = sum / (yrs*12)  #calculating the monthly average
        sum = format((sum), ".2f")
        print(f'The total rainfall was {(sum)} inches.')
        m_avg = format(m_avg, ".2f")  #formatting code
        print(f'The monthly average rainfall was {(m_avg)} inches.')


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
