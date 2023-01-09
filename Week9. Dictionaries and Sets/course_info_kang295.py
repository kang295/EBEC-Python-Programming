"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 09.3 - Course Info
Date: 11/07/2022

Description:
    This program generates the nested dictionary and gets the input to show the course information

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

def get_course_data():
    nested_dict = {'CS101': {'room': '3004', 'instructor': 'Django', 'time': '9:00 a.m.'},  #making a nested dict with given information
    'CS102': {'room': '4501', 'instructor': 'Idle', 'time': '10:00 a.m.'},
    'CS103': {'room': '6755', 'instructor': 'Rich', 'time': '11:00 a.m.'},
    'NT110': {'room': '1244', 'instructor': 'Marshal', 'time': '12:00 p.m.'},
    'CM241': {'room': '1411', 'instructor': 'Pickle', 'time': '2:00 p.m.'}}
    return nested_dict
    
def main():
    dict = get_course_data()
    name = input("Enter a course number: ")

    if name in dict:  #check if the input key is valid or not
        print(f"  The details for course {name} are:")
        print(f"    Instructor: {dict[name]['instructor']}")
        print(f"          Room: {dict[name]['room']}")
        print(f"          Time: {dict[name]['time']}")
          
    else: 
        print(f"  {name} is an invalid course number.") #alert message showing that course is invalid



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
