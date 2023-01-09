"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 09.1 - Capital Quiz
Date: 11/06/2022

Description:
    This program gets the data and store it as dictionary with the state names as keys and the state capitals 
    as values. Then, the program will quiz the user to enter the capital for a particular state.

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

def get_state_data():  #function storing txt file as dictionary with keys and values
    dict = {}
    with open("state_capitals.txt") as file:
        for line in file:
            s = line.strip().split(", ")
            dict[s[1]] = (s[0])
    return dict
    
def main():
    dict = get_state_data()
    keys = list(dict.keys()) #storing only keys into the list
    cnt = 0
    cor = 0
    random.shuffle(keys) #shuffling random key values

    while len(keys) > 0:
        key = keys.pop(0) #the first deleted element of a list
        answer = input(f"What is the capital of {key} (enter 0 to quit)? ")
        
        if answer == '0':
            break
        cnt += 1

        if answer.title() == dict[key]: #making the input non-case sensitive
            print("  That is correct!")
            cor += 1

        if answer.title() != dict[key]:
            print("  That is incorrect.")
            print(f"  The capital of {key} is {dict[key]}.")
            keys.append(key)

    print(f"You answered {cor} out of {cnt} questions correctly.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
