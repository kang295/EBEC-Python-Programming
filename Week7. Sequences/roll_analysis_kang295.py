"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 07.3 - Roll Analysis
Date: 10/24/2022

Description:
    This program rolls two six sided dice and get the sum of two numbers. Then, the sums are
    appended in the list for multiple times. Lastly, the frequency rate will be calculted.

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
import random

"""Write new functions below this line (starting with unit 4)."""

def roll_d6():  #getting random number from 1 to 6
    first = random.randint(1,6)
    return first 

def get_2d6_rolls(times):  #getting the sum of two random dice numbers and append it to the list
    list = []
    for i in range(times):
        a = roll_d6()
        b = roll_d6()
        sum = a + b
        list.append(sum)
        i += 1
    return list

def main():
    iterate = 1000000
    save = get_2d6_rolls(iterate)
    print('Roll  Frequency')
    for i in range(2, 13):  #checking the frequency percentage for specific number in a list
        formatted = "{:.2f}".format(save.count(i) / iterate * 100) #formatting
        if i > 9: 
            print(f' {i}     {formatted}%') 
        elif (i > 4) and (i < 10):
            print(f'  {i}    {formatted}%') 
        else:
            print(f'  {i}     {formatted}%') 
        i += 1


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
