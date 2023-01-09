"""
Author: Hyoju Kang, kang295@purdue.edu
Assignment: 06.3 - Random Vowels
Date: 10/21/2022

Description:
    This program is a module for drawing each vowels

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
from turtle import *


"""Write new functions below this line (starting with unit 4)."""


def draw_a():
    """Complete this function to draw the character a."""
    setheading(0)  #turn to position 0 degree
    pendown()   #draw when moving
    circle(30)   #draw a circle
    circle(30,90)  #angular distance only 90 degrees
    forward(30) #move forward 
    right(180)  #turn cw 180 degrees
    forward(60) #move forward 
    penup()  #do not draw when moving
    left(90)  #turn ccw 90 degrees
    forward(10)  #move forward 
    penup()
    setheading(0)
    forward(50)

def draw_e():
    """Complete this function to draw the character e."""
    penup()
    setheading(90)
    forward(50)
    pendown()
    setheading(0)
    forward(60)
    right(270)
    circle(30,180)
    circle(30,150)
    penup()
    setheading(0)
    forward(50)



def draw_i():
    """Complete this function to draw the character i."""
    forward(20)
    pendown()
    setheading(90)
    forward(60)
    penup()
    forward(20)
    pendown()
    circle(1)
    penup()
    setheading(270)
    forward(80)
    left(80)
    forward(30)
    penup()
    setheading(0)
    forward(50)


def draw_o():
    """Complete this function to draw the character o."""
    setheading(0)
    forward(40)
    pendown()
    circle(30)
    penup()
    forward(75)

def draw_u():
    """Complete this function to draw the character u."""
    setheading(90)
    forward(45)
    pendown()
    setheading(90)
    forward(35)
    setheading(270)
    forward(35)
    circle(20,180)
    forward(35)
    left(180)
    forward(60)
    setheading(0)
    penup()
    forward(50)

def start():
    """This function initializes the window and the turtle.
    Do not modify this function or any of the properties it sets.
    """
    setup(600, 400)
    width(9)
    speed(0)
    penup()
    goto(-220, -30)


def main():
    """You can use this function for your own testing. It will not be checked
    by the auto-grader."""
    draw_a()
    draw_e()
    draw_i()    
    draw_o()
    draw_u()

"""Do not change anything below this line."""
if __name__ == "__main__":
    start()
    main()
    done()
