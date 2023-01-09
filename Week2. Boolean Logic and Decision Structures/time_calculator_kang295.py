"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 02.4 - Time Calculator
Date: 09/08/2022

Description:
    This program calulates the proper expression of time when only time seconds are given
    

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

    value = int(input('Please enter a time in seconds: ')) #getting input and store the value

    day = value // 86400     #converting and getting required value
    hours = value % 86400 //3600
    minutes = value % 3600 // 60
    sec = value - (3600*hours + 86400*day + 60*minutes)

    if (value//60) < 1:  #case1
        print(f'  {(value)} seconds is less than one minute.')
        return 
    if (value//60) == 1:  #case2
        print(f'  {(value)} seconds equals 1 minute(s).') 
        return
    
    change = '{:,.0f}'.format(value)  #change to formal number expression

    print(f'  {(change)} seconds equals ', end = '') 

    if day > 0 and hours > 0 and minutes > 0 and sec >0:    #when converted to all the values
        print(f'{day} day(s), {hours} hour(s), {minutes} minute(s) and {sec} second(s)', end = '')
        print('.')
        return

    if day > 0: #each expression
        print(f'{day} day(s)', end ='')
        if (hours > 0 and minutes > 0) or (hours > 0 and sec > 0) or (minutes > 0 and sec > 0):
            print(', ', end ='')
        if (hours > 0 and minutes <= 0 and sec <= 0) or (hours <= 0 and minutes <= 0 and sec > 0) or (hours <= 0 and minutes > 0 and sec <= 0):
            print(' and ', end ='')
    if hours > 0:  
        print(f'{hours} hour(s)', end ='')
        if (minutes > 0 and sec > 0):
            print(', ', end ='')
        if (minutes <= 0 and sec > 0) or (minutes > 0 and sec <= 0):
            print(' and ', end ='')
    if minutes > 0:
        print(f'{minutes} minute(s)', end ='')
        if sec > 0:
            print(' and ', end ='')
    if sec > 0:
        print(f'{sec} second(s)', end ='')
    print('.')



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
