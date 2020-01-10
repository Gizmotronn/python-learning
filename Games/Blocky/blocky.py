import pygame # pygame module pip
import sys
import random

# https://www.youtube.com/watch?v=-8n91btt5d8

# Initialize pygame
pygame.init()

WIDTH = 800
HEIGHT = 600

# Game screen
screen = pygame.display.set_mode((WIDTH, HEIGHT)) # game screen is 800px*600px and the variable "screen" is used for this

# Game Loop
game_over = False

while not game_over: # while the game is not over (which will be "over" when the player closes/dies), do this loop

    for event in pygame.event.get(): # Track events that occur (mouse, keyboard) when the game is open
        # print(event)

            if event.type = pygame.QUIT:
                sys.exit() # system exit