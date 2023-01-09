"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 04.5 - Prime List
Date: 10/03/2022

Description:
    This program lists all the prime numbers between 2 and input itself

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
from math import sqrt

"""Write new functions below this line (starting with unit 4)."""

def is_prime(value): #prime number function that determines if it is prime or not
    pr = False
    if value == 2:
        pr = True  #2 is a prime number
    if value > 2:
        pr = True
        for i in range(2, int(sqrt(value))+1):  #this allows te function goes through all number except for 1 and itself
            if (value % i) == 0:
                pr = False
                break
            
    return bool(pr) #returning boolean expression

def list_prime(start, end):
    pr_list = [ ]
    
    for i in range(start, end+1):
        if is_prime(i):
            add = i
            pr_list.append(add)
                
    return pr_list

def main():
    value = int(input('Enter a positive integer: '))
    if value == -1:  #exit the function when value is -1
        return

    list = list_prime(2, value)
    print(f'The primes up to {value} are:', end=' ')
    my_string = ', '.join(map(str, list)) 
    print(''.join(my_string))

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
