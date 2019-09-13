import pygame, sys # import pygame libraries into program, so we can access them. Also importing the sys libaries which are used to exit the game
from pygame.locals import *

# Controlling the speed (FPS) of the program
FPS = 200 # Change this value to slow down/speed up game

# Global variables used throughout the program
# Game window
WINDOWWIDTH = 400
WINDOWHEIGHT = 300

# Writing the main function of the Pong program
def main(): # declaring the function - main function
    pygame.init() # initialising pygame
    global DISPLAYSURF # Creates the main surface that will be used throughout the program. Pygame draws objects onto surfaces