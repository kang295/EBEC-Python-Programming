"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 02.2 - Software Sales
Date: 09/07/2022

Description:
    This program gets the number of package as input and calculates the discounted cost
    

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
    num = int(input('How many packages will be purchased: ')) #getting input and store the value
    
    if num < 1: #checking how many packages user wants
        print('  Invalid Input!') #printing

    elif (num >= 1) and (num <= 3): 
        print('  No discount applied.') 
        cost = num * 880 #calculating the cost
        cost = "${:,.2f}".format(cost) #making two decimal
        print(f'  The total price to purchase {(num)} packages is {(cost)}.') 
    
    elif (num >= 4) and (num <= 39): 
        cost = num * (880*0.9) 
        cost = "${:,.2f}".format(cost) 
        print('  10% discount applied.') 
        print(f'  The total price to purchase {(num)} packages is {(cost)}.')  

    elif (num >= 40) and (num <= 199):  
        cost = num * (880*0.85) 
        cost = "${:,.2f}".format(cost) 
        print('  15% discount applied.') 
        print(f'  The total price to purchase {(num)} packages is {(cost)}.')  

    elif (num >= 200) and (num <= 999):  
        cost = num * (880*0.70) 
        cost = "${:,.2f}".format(cost) 
        print('  30% discount applied.') 
        print(f'  The total price to purchase {(num)} packages is {(cost)}.') 

    else:  
        cost = num * (880*0.58) 
        cost = "${:,.2f}".format(cost) 
        print('  42% discount applied.') 
        print(f'  The total price to purchase {(num)} packages is {(cost)}.') 

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
