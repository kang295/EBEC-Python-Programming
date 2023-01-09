"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 08.4 - Number Writer
Date: 11/04/2022

Description:
    This program asks the user how many numbers it should generate and then writes that
    many random numbers to a file named random_numbers.txt. Each random number should
    be in the range of 1019 through 1215 inclusive.

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
import random
"""Write new functions below this line (starting with unit 4)."""


def main():
    outfile = open('random_numbers.txt', 'a+') #file generation
    count = int(input("How many numbers would you like? "))
    for i in range(count):
        num = random.randint(1019, 1215) #assigning the range of random number
        outfile.write(f"{num}\n") #saving each number as new line
    outfile.close()

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
