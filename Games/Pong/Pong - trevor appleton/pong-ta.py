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

# Global Variables
    # Window Size
WINDOWWIDTH = 400    
WINDOWHEIGHT = 300

# Main Function
def main():
    pygame.init # Initialize pygame
    global DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) # set the size of the display, or window, to the values set in "WINDOWHEIGHT", "WINDOWWIDTH"
    pygame.display.set_caption('Pong by ACORD') # Setting the caption, or title, of the window