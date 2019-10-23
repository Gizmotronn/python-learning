# https://pythonprogramming.net/pygame-python-3-part-1-intro/

import pygame # imports the pygame library
from pygame import pygame

pygame.init() # init.ialises pygame, allows the usage of commands from pygame

# Setting Display for the Arena/Surface/Display
gameDisplay = pygame.display.set_mode((800,600)) # sets the display to be 800px*600px. This is a tuple  
pygame.display.pygame.display.set_caption('A little bit Racy', icontitle=None) # sets window title/caption

clock = pygame.time.Clock() # game clock, used to track time within the game, FPS (frames per second)

# Crash/Quit Loop
crashed = False # sets the state of the game (crashed)

while not crashed:
    
    for event in pygame.event.get(): # nothing in function ()
        if event.type == pygame.quit: # there are a number of python/pygame events, one of these is "quit". User exits out of window
            crashed = True # sets the  crashed state to true

        print(event)

    pygame.display.update()  # updates specific areas of the screen. If there are no parameters in the paranthesis of the function, the entire screen will be updated
    clock.tick(60)

    pygame.quit()
    quit()