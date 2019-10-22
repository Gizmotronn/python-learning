# Pong - Trevor Appleton
# http://trevorappleton.blogspot.com/2014/04/writing-pong-using-python-and-pygame.html

"""
CONTENTS:
Line 9: Creating a blank screen
"""

# Creating a blank screen

import pygame, sys # imports the pygame library & sys
"""
Import pygame - pygame libraries, for python applications. pygame draws directly onto the screen/display (variable: displaysurf)
import sys - sys libraries, used to exit the game
import pygame, sys can be done on separate lines
"""
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
    global DISPLAYSURF # display surfac

    FPSCLOCK = pygame.time.Clock() # this means that the clock will run at the value that we set in the variable FPS (see line 43)
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT)) # set the size of the display, or window, to the values set in "WINDOWHEIGHT", "WINDOWWIDTH"
    pygame.display.set_caption('Pong by ACORD') # Setting the caption, or title, of the window

    while true: # main game loop. It keeps running until the game ends
        for event in pygame.event.get():
            if event.type == QUIT: # set what happens if the "quit" event is triggered
                pygame.quit()
                sys.exit()

        pygame.display.update() # asking the screen to update (for example if something is drawn it won't? show unless the screen is updated)
        FPSCLOCK.tick(FPS) # see line 32

if __name__=='__main__': # calling in the main function (line 36)
    main()                