"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 09.2 - World Series
Date: 11/06/2022

Description:
    This program makes two dictionaries from given text file. One with 
    name as key and number of winning as value. The other with years as key and
    team that won that year as value.

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
from collections import Counter
"""Write new functions below this line (starting with unit 4)."""

def load_winners_data():
    dict1 = {}
    dict2 = {}
    year_list = [*range(1903, 2022, 1)]  #making year list from 1903 to 2022
    year_list.remove(1904)
    year_list.remove(1994)

    with open("WorldSeriesWinners.txt") as file:
        content_list = file.readlines()
    content_list = [x.strip() for x in content_list]  #making team name only list

    dict2 = dict(zip(year_list, content_list)) #name and number of winning of a team
    dict1 = dict(Counter(dict2.values())) #counting the number of winning and putting it as values to dictionary 1

    return dict1, dict2
    
def main():
    dict1, dict2 = load_winners_data()
    year = int(input("Enter a year in the range 1903 -- 2021: "))
    if year < 1903 or year > 2021:
        print(f"  Data for the year {year} is not included in this system.")
    if year == 1904 or year == 1994:
        print(f"  The World Series wasn't played in the year {year}.")

    if year > 1902 and year < 2022 and year != 1904 and year != 1994:
        print(f"  The {dict2[year]} won the World Series in {year}.")
        cnt = dict1[dict2[year]]
        print(f"  They have won the World Series {cnt} times.")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
