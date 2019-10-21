# Pong - Trevor Appleton
# http://trevorappleton.blogspot.com/2014/04/writing-pong-using-python-and-pygame.html

"""
CONTENTS:
Line 9: Creating a blank screen
"""

# Creating a blank screen

import pygame, sys # imports the pygame library & sys
from pygame.locals import *

# Number of Frames/Second
FPS = 200

# Main Function
def main():
    pygame.init # Initialize pygame