"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 08.1 - Pig Latin
Date: 11/01/2022

Description:
    This program gets string input and convert it to Pig Latin.

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

def pig(str):  #function that transform input to Pig Latin
    list = str.split()  #sting into list
    for i in range(len(list)):
        list[i] = list[i][1:] + list[i][0] + 'ay'
    mystring = ' '.join(list)  #list to string
    latin_cap = mystring.capitalize() 
    return latin_cap


def main():
    str = (input("Enter a string: "))
    latin = pig(str)
    print(f"Pig latin: {latin}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
