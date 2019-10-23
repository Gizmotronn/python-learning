# https://pythonprogramming.net/pygame-python-3-part-1-intro/

import pygame # imports the pygame library

pygame.init # initialises pygame, allows the usage of commands from pygame

# Setting Display for the Arena/Surface/Display
gameDisplay = pygame.display.set_mode((800,600)) # sets the display to be 800px*600px. This is a tuple  
pygame.display.pygame.display.set_caption('A little bit Racy', icontitle=None) # sets window title/caption

clock = pygame.time.Clock() # game clock, used to track time within the game, FPS (frames per second)
