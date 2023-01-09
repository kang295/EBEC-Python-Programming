"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 09.4 - File Analysis
Date: 11/07/2022

Description:
    This program sorted a unique words, common words and word used at one file from 
    two different text files. It then outputs four different text files. 

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
from collections import Counter
from string import punctuation
import string
import re
"""Write new functions below this line (starting with unit 4)."""



def read_save():  #this reads and saves the given two text files with paragraphs

    with open('python_1.txt') as file:
        list1 = file.read().split()
        list1 = [re.sub(r"(^[^\w]+)|([^\w]+$)", "", x) for x in list1] #get rid of punctuations in front and back of the words
        word_lower1 = [] #initializing a new list for word list from given text file
        for word in list1:
            word_lower1.append(word.lower())
    with open('python_2.txt') as file:
        list2 = file.read().split()
        list2 = [re.sub(r"(^[^\w]+)|([^\w]+$)", "", x) for x in list2] 
        word_lower2 = []
        for word in list2:
            word_lower2.append(word.lower())

    list1 = dict(Counter(word_lower1))
    list2 = dict(Counter(word_lower2))
 
    with open("python_1_word_frequency.txt",'w') as file:  #generating a new text file
        for key, value in sorted(list1.items()):   #alphabetical order for the list
            file.write('%s: %s\n' % (key, value))

    with open("python_2_word_frequency.txt",'w') as file: 
        for key, value in sorted(list2.items()): 
            file.write('%s: %s\n' % (key, value))

    return(word_lower1, word_lower2)

def common(word1, word2):
    word3 = list(set(word1) & set(word2)) #it only finds the list of intersected words
    with open('common_words.txt', 'w') as file:
        for item in sorted(word3):
            file.write("%s\n" % item)
    return

def diff(word1, word2): #function for only obtaining words that are used only in one of the lists
    diff_word = list(set(word1).symmetric_difference(set(word2))) #this finds the distinct word that is used only in one list
    with open('eitherbutnotboth.txt', 'w') as file:
        for item in sorted(diff_word):
            file.write("%s\n" % item)

def main():
    word1, word2 = read_save()
    common(word1,word2)
    diff(word1, word2)
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
