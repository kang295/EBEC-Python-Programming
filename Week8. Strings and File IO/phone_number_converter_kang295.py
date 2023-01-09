"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 08.2 - Phone NUmber Converter
Date: 11/03/2022

Description:
    This program gets phone number string mixed with character and output only with numbers

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

def convert_number(str):
    new = str.lower() #make every string lowercase
   
    #change letters to numbers
    replace = {'a': '2', 'b': '2','c': '2'}
    new = new.translate(str.maketrans(replace)) #changing command
    replace = {'d': '3', 'e': '3','f': '3'}
    new = new.translate(str.maketrans(replace))
    replace = {'g': '4', 'h': '4','i': '4'}
    new = new.translate(str.maketrans(replace))
    replace = {'j': '5', 'k': '5','l': '5'}
    new = new.translate(str.maketrans(replace))
    replace = {'m': '6', 'n': '6','o': '6'}
    new = new.translate(str.maketrans(replace))
    replace = {'p': '7', 'q': '7','r': '7', 's': '7'}
    new = new.translate(str.maketrans(replace))
    replace = {'t': '8', 'u': '8','v': '8'}
    new = new.translate(str.maketrans(replace))
    replace = {'w': '9', 'x': '9','y': '9', 'z': '9'}
    new = new.translate(str.maketrans(replace))

    return new

def main():
    str = (input("Enter a telephone number: "))
    con = convert_number(str)
    print(f"The phone number is {con}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
