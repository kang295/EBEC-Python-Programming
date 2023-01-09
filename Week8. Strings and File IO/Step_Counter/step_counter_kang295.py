"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 08.6 - Step Counter
Date: 11/05/2022

Description:
    This program write the file containing every day step and calculate, display the average number
    of steps taken for each month. 

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
    print('The average steps taken each month were:')
    file = open("steps.txt")
    data = file.read()
    list = data.split("\n") #storing values into a list
    list = list[:-1] #eleminating the last element
    
    res = [eval(i) for i in list] #making all string values into inegers

    print(f"   January : {(sum(res[0:30 + 1]) / 31):.2f}") #calculation for average steps for each month
    print(f"  February : {(sum(res[31:58 + 1]) / 28):.2f}")
    print(f"     March : {(sum(res[59:89 + 1]) / 31):.2f}")
    print(f"     April : {(sum(res[90:119 + 1]) / 30):.2f}")
    print(f"       May : {(sum(res[120:150 + 1]) / 31):.2f}")
    print(f"      June : {(sum(res[151:180 + 1]) / 30):.2f}")
    print(f"      July : {(sum(res[181:211 + 1]) / 31):.2f}")
    print(f"    August : {(sum(res[212:242 + 1]) / 31):.2f}")
    print(f" September : {(sum(res[243:272 + 1]) / 30):.2f}")
    print(f"   October : {(sum(res[273:303 + 1]) / 31):.2f}")
    print(f"  November : {(sum(res[304:333 + 1]) / 30):.2f}")
    print(f"  December : {(sum(res[334:364 + 1]) / 31):.2f}")
    file.close()


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
