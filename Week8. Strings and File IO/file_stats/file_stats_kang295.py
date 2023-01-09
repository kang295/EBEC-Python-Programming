"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 08.3 - File Stats
Date: 11/04/2022

Description:
    This program reads the contents of a file and determines the number of words
    in the file, the number of lines in the file, and average number of words per line.

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
    word_num = 0 #assigning initial number
    line_num = 0
    with open('frontiero_v_richardson.txt') as file:  #open the file
        for line in file:
            words = line.split() #words in a line are counted 
            word_num += len(words) 
            line_num += 1  #counts the number of line 

    print(f"Total number of words: {word_num}")
    print(f"Total number of lines: {line_num}")
    print(f"Average number of words per line: {(word_num / line_num):.1f}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
