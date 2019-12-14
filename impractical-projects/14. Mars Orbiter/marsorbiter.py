# Program Contents:
"""
Lines 8-11: Pip Imports
Lines 13-17: Colour Codes/Colour Table
Lines 19-  : Satellite Class & Initialization Method
"""

import os # importing the following packages/python modules; pygame is installed via pip. // Game launches in full screen, but there are options to escape (esc key) to a window. // The "OS" module allows the player to control the window after the "esc" key is pressed
import math # For gravity and trigonometric functions/calculations
import random # to start the satellite off with a random position and velocity
import pygame as pg

WHITE = (255, 255, 255) # sets colour code for white variable (hex code) - 255, 255, 255 = white
BLACK = (0, 0, 0) # sets the colour code for black to 0, 0, 0
RED = (255, 0, 0)
GREEN = (0, 255, 0)
LT_BLUE = (173, 216, 230)

class Satellite(pg.sprite.Sprite): # creates a class object - Satellite Object // Uses pygame (pg, see importing modules) to create a sprite - using the pg.sprite.Sprite function // Defines class object.
    # Satellite object // Rotates to face planet // Crashses & Burns - nostarch.com
    # It is passed through pygame (pg) so that any object in this class will be sprites

    def __int__(self, background): # initializes object    
        super().__init__()
        self.background = background # needs to pass the class a background object
        self.image_sat = pg.image.load("satellite.png").convert() # uses pygame to load the "satellites.png" img file in this directory by using pg.image.load, and sets the image_sat (image of satellite) to this
        self.image_crash = pg.image.load("satellite_crash_40x33.png").convert() # // And converts it  "//" continuing on from above line comments // Convert function converts image into a graphic format that pygame can run efficiently when the game loop starts
        self.image = self.image_sat
        self.rect = self.image.get_rect()
        self.image.set_colorkey(BLACK) # sets transparent colour - colour hex code (0, 0, 0) - defined in Colour Codes/Colour Table (see Program Contents)
