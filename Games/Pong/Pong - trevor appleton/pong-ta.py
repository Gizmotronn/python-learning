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

    while true: # main game loop
        for event in pygame.event.get():
            if event.type == QUIT: # set what happens if the "quit" event is triggered
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()                