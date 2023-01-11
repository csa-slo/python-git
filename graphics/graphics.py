#!/usr/bin/python
from os import get_terminal_size
from time import sleep

# Draw one line graphics with given string to animate, starting position, trajectory
def one_line_graphics(image, position, trajectory):

    # Get terminal size
    term_size = get_terminal_size()

    # Draw loop
    while True:

        # Draw a frame
        print(" " * position + image)

        # Calculate position for next frame
        position = trajectory(position, image, term_size)

        # Limit framerate to 60FPS
        sleep(1/60)

        # Clear the terminal
        print("\n" * term_size.lines)

# Specify a constant speed of motion
def constant_velocity(position, image, term_size):
        if (position + len(image)) % term_size.columns == 0:
            position = 0
        else:
            position += 1
        return position

# Main
initial_position = int(input("Enter starting position: "))
initial_image = input("Enter an image: ")
one_line_graphics(initial_image, initial_position, constant_velocity)