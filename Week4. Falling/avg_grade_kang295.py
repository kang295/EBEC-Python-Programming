"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 04.3 - Avg Grade
Date: 10/02/2022

Description:
    This program gets 5 inputs and displays letter grade for each one. Also, it calculates the average score of five grades
    and displays letter grade.
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
def get_valid_score():   #function for getting valid grade from 0 to 100
    score = float(input('Enter a score: '))
    for i in range(5):
        while score < 0 or score > 100:  #displaying error message when number is not valid
            print('  Invalid Input. Please try again.')
            score = float(input('Enter a score: '))
    return score

def calc_average(arr):  #calculating average number with 5 inputs
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
    count = len(arr)
    avg = sum / count

    return avg 

def determine_grade(avg):  #determining the letter grade with average number
    arr3 = ''
    if avg >= 92 and avg <= 100:
        arr3 = 'A'
    elif avg >= 82 and avg < 92:
        arr3 = 'B'
    elif avg >= 73 and avg < 82:
        arr3 = 'C'
    elif avg >= 64 and avg < 73:
        arr3 = 'D'
    else:
        arr3 = 'F'

    return arr3

def main():
    arr = [0,0,0,0,0]  #setting the initial array with 0
    for i in range(5): #displaying the input value each time
        score = get_valid_score()
        grade = determine_grade(score)
        print(f'  The letter grade for {(score):.1f} is {(grade)}.')
        arr[i] = score #replacing the 0 inside the array with valid input

    avg = calc_average(arr)
    grd = determine_grade(avg)
    new = format(avg, ".2f")
    print('')
    print('Results:')
    print(f'  The average score is {(new)}.')
    print(f'  The letter grade for {(new)} is {grd}.')

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
