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
        self.x = random.randrange(315, 425) # sets the x coordinate of the object (using random py module) to anywhere in the range of x = 315-425
        self.y = random.randrange(70,180) # does the same thing as above line, just with the y-axis
        self.dx = random.choice([-3, 3]) # Randomly sets the velocity of the class object to -3, 3 (x) // Neg values (-) - counter/anticlockwise orbit // Pos values (+/ ) - clockwise orbit 
        self.dy = 0 # delta y. // Eventually the gravity module (import section) will establish dy values
        self.heading = 0 # initialises satellite's dish orientation // Satellite dish should always point towards Mars // This needs to overcome inertia (more to come for this)
        self.fuel = 100
        self.mass = 1
        self.distance = 0 # initialises distance between satellite object and planet
        self.thrust = pg.mixer.Sound('thurst_audio.ogg') # uses pygame(pg).mixer.Sound to use the "thrust_audio.ogg" sound file as the file of choice for self.thrust function // It is in .ogg rather than .mp3/other format because .ogg works well with python and pygame
        self.thrust.set_volume(0.07) # Sets the volume of the audio file (above line) to 7% (0.07) // 1 = 100%, 0 = 0%

