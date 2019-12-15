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

    def thruster(self, dx, dy): # defines thruster function for the Satellite class object
        self.xd += dx # sets the value for delta x for the thruster object
        self.dy += dy
        self.fuel -= 2 # when thruster is used, empties the fuel tank of the satellite slightly // thruster function in satellite class object // fuel function
        self.thrust.play() # makes the hissing sound // Call play() method 

    def check_keys(self): # takes self as an argument // defines check_keys (like getKeyDown in Unity/C#) function
        keys = pg.key.get_pressed() # uses pygame to detect which key was pressed, sends this to the keys variable

        # Firing thrusters
        if keys[pg.K_RIGHT]: # if key pressed call thruster() method/function, pass it some dx and dy values (see below). // this is the same for the elifs in this block as well
            self.thruster(dx=0.05, dy=0) # sets what happens if right arrow is pressed - dx is change by +0.05, dy (delta y) is still set to 0 (initialized value)
        elif keys[pg.K_LEFT]: # uses pygame (pg)
            self.thruster(dx=-0.05, dy = 0)  
        elif keys[pg.K_UP]:
            self.thruster(dx=0, dy=-0.05)  
        elif keys[pg.K_DOWN]:
            self.thruster(dx=0, dy=0.05)      

    # Locating the Satellite

    def locate(self, planet): # defines locate function/method for self, and planet // Self refers to the Satellite // Locating the satellite - calculates the distance of the satellite from the planet // Then determines the heading for pointing the dish at the planet // The locate mmethod needs to be passed the satellite (self) and the planet objects
        px, py = planet.x, planet.y # for determining the distance between the planet and self objects in space (next 2 lines)
        dist_x = self.x - px # the distance (x-coord) is the x coord of the self minus the coord of the planet's x
        dist_y = self.y - py # same thing as above line

        # getting direction to planet to point the dish of the satellite
        planet_dir_radians = math.atan2(dist_x, dist_y) # calculate angle between the satellite's heading and the planet // So that you can rotate the satellite dish towards the planet
        self.heading = planet_dir_radians * 180 / math.pi
        self.heading -=90 # sprite is travelling tail first // In pygame, the front of a sprite is to the east (default) - self object is orbiting planet object tail-first // You need to subtract 90 degrees from the heading for the dish to point towards the planet object (Mars) - neg angles return clockwise rotation in pygame of objects (in this case self)
        self.distance = math.hypot(dist_x, dist_y) # uses math's module - hypotunese function - to calculate the distance // Get the Euclidian distance between both objects

     # Rotating the satellite and drawing its orbit

     def rotate(self): # pygame - rotate self game object by passing it the rotate(self): method
         # Rotates satellite using degrees so the dish faces the planet
         self.image = pg.transform.rotate(self.image_sat, self.heading) # the self.image function is equal/set to pygame rotating (a transformation - maths) the image_sat of self, and the heading of the self object // Rotates the IMAGE of the satellite (which is part of the self object)
         self.rect = self.image.get_rect() # end the function be getting the transformed image's rect object

         # Update satellite's position & draw line to face orbital path
         last_center = (self.x, self.y)
         self.x += self.dx # sets the x coordinate of the self object using delta (physics)
         self.y += self.xy # delta y/delta x (above line)
         pg.draw.line(self.background, WHITE, last_center, (self.x, self.y)) # the orbital line/path