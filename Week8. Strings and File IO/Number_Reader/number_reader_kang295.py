"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 08.5 - Number Reader
Date: 11/04/2022

Description:
    This program reads the random numbers from the random_numbers.txt file I cre-
ated in Exercise 08.4 - Number Writer. The program should then calculate and display the
following data about the numbers in the file

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
    list = []
    minimum = 0 #initializing the value
    maximum = 0
    sum = 0
    avg = 0
    file = open("random_numbers.txt") #opening file
    for line in file:
        list.append(int(line)) #saving each line element as interger in a list
    for i in range(len(list)):
        sum += list[i] 
    avg = sum / len(list) 
    minimum = min(list)
    maximum = max(list)
    file.close() #closing file
    print(f"{(len(list)):,} numbers were read from the file.")
    print(f'Min: {(minimum):,}')
    print(f'Max: {(maximum):,}')
    print(f'Sum: {(sum):,}')
    print("Avg: {:.1f}".format(avg))


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
