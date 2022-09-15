#!/usr/bin/python
from os import get_terminal_size
from time import sleep

# Initialize constants
position = int(input("Enter starting position: "))
image = input("Enter an image: ")

# Draws an  
def one_line_graphics(position, trajectory, image):

    #Get terminal size
    term_size = get_terminal_size()

    #Draw loop
    while True:

        #Draw the current frame
        print(" " * position + image)

        #Limit framerate to 60FPS
        sleep(1/60)

        #Clear the terminal
        print("\n" * term_size.lines)

        #Calculate next position
        position = trajectory(position, image, term_size)

def constant_velocity(position, image, term_size):
        if (position + len(image)) % term_size.columns == 0:
            position = 0
        else:
            position += 1
        return position

one_line_graphics(position, constant_velocity, image)
