import pygame # as pg //#/ Importing the pygame python module into this script
pygame.init() # Initialises pygame

win = pygame.display.set_mode((500, 500)) # uses the pygame module to create a window, called win, that is 500px*500px

pygame.display.set_caption("Pygame") # sets the window caption or title

# Loading images/sprites
# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('R1.png'), pygame.image.load('Img/R2.png'), pygame.image.load('Img/R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')] # list
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')] # You COULD flip the images, but that's not what's happening here :)
bg = pygame.image.load('bg.jpg') # background images
char = pygame.image.load('standing.png') # the character when there is no movement // i.e. he is standing still

# Clock
clock = pygame.time.Clock() # replaces "import time" return "time.sleep(1)" for e.g. // Pygame clock/time

# Screen/Window Dimensions
screenWidth = 500 # the screen is set to 500 pixels wide and 480 pixels tall (see below line)
screenHeight = 480 

# Character/Player Attributes
class player(object): # create a class --> object oriented programming
    def __init__(self, x, y, width, height):
        self.x = x # x coord of the "self" // player
        self.y = y
        self.width = width # Character Attributes --> man = player(self.attribute values) in Main Game Loop
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0 # See end of document to see what it looked like without object oriented
        self.standing = True # standing still
        self.centrePointX = self.x
        self.centrePointY = self.y
        self.rotate = False

    def draw(self, win): # argument of the window
        if self.walkCount + 1 >= 27: # frame rate 
            self.walkCount = 0

        if not(self.standing): # if the character is not standing still, he will be facing to the left, or to the right, depending on the direction he moved in first. // This is so that the bullets "know" where to go as well as for just aesthetics and neatness
            if left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif right: 
                win.blit(walkRight[walkCount//3], (self.x,self.y))      # integer remainder
                self.walkCount += 1
        else: 
            if self.right:
                win.blit(walkRight[0], (self.x, self.y)) # index value for images/sprites 
            else: 
                win.blit(walkLeft[0], (self.x, self.y))

class enemy(object):
	walkRight = [pygame.image.load('R1E.png'), pygame.image.load('R2E.png')] # etc
	walkLeft = [pygame.image.load('R2E.png')] # etc 

	def __init__(self, x, y, width, height, end):
	self.x = x
	self.y = y
	self.width = width
	self.height = height
	self.end = end 
	self.walkCount = 0
	self.vel = 3
	self.path = [self.x, self.end] # where we start, where we end/enemy    

	def draw(self,win):
		self.move() # every time we draw, we first move and then draw the character/enemy
		# pass
		if self.walkCount + 1 >= 33:
			self.walkCount = 0
	
		if vel > 0 # moving right // velocity is positive # / 3
			win.blit(self,walkRight[self.walkCount //3], (self.x, self.y))
			walkCount += 1 
		else:
			win.blit(self,walkLeft[self.walkCount //3], (self.x, self.y))
			walkCount += 1        

	def move(self)
		if self.vel > 0: # move right
			if self.x + self.vel < self.path[1] + self.vel # if it hasn't moved too far to the right // [1] refers to the tuple/list index value
				self.x += self.vel
			else: # change directions	
				self.vel = self.vel * -1
				self.walkCount = 0
		else: # if velocity is negative
			if self.x - self.vel > self.path[0]:
				self.x += self.vel # velocity is now negative
			else:
				self.vel = self.vel * -1
				self.walkCount = 0
		#pass
    
# Projectiles/Bullets
class projectile(object): # object oriented --> projectile object
    def __init__(self,x,y,radius,color,facing):
        self.x = x 
        self.y = y
        self.radius = radius 
        self.color = color
        self.facing = facing
        self.vel = 8 * facing # determines whether the projectile will move left or right; // 8 is part of the magnitude (facing is direction); so that it would move 8 pixels per second (for example)

    def draw(self, win): # drawing the projectile/bullet
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius) # ,1 before the close bracket makes the circle not filled in    

# Redraw Game Window Function
"""This is so that the screen refreshes (see in the main game loop); without this nothing would happen after the initial blit?"""
def redrawGameWindow():
	win.blit(bg, (0,0))
	man.draw(win)
	goblin.draw(win) # draw "goblin" enemy on the window // game window
	for bullet in bullets:
		bullet.draw(win)
	
	pygame.display.update()

# main loop
man = player(200, 410, 64, 64)
goblin = enemy(100, 410, 64, 64, 450) # starts at x = 100, goes right until x = 450bullets = [] # list --> projectiles//
run = True
while run == True:
    clock.tick(27) # FPS Set to 27

    for event in pygame.event.get(): #makes use of the module's event get feature 
        if event.type == pygame.QUIT: # if the player closes the game
            run = False # set the main game loop to false // Boolean
    for bullet in bullets: # for every bullet inside the "bullets"list
        if bullet.x < 500 and bullet.x > 0: # bullet not going off screen // Bullet coordinates (property of x, projectile class object)
            bullet.x += bullet.vel # allows the bullet to be shot // moves by the vel every second (see pygameClock/pyClock)
        else: # bullet is off screen // As this is looking at each indivdual bullet, it will only "pop" the one that is off screen, this function can? run the same/both options at the same time...
            bullets.pop(bullets.index(bullet)) # pop = remove element            

    keys = pygame.key.get_pressed() # makes use of the module's ability to detect the key that the player presses down on. // Pygame can also look at mouse movement

    if keys[pygame.K_SPACE]:
        if man.left:
            facing = -1 # boolean//man/player is facing left // Affects other stuff now // Negative direction
        else:
            facing = 1
        if len(bullets) < 5: # How many bullets we want the maximum amount to be
            bullets.append(projectile(round(man.x + man.width // 2), round(man.y + man.height//2), 6, (0,0,0), ))# append --> add to the end of the list // Projectile object attributes

    if keys[pygame.K_LEFT] and man.x > man.vel: # left arrow key    // Solving the problem with character moving off the screen
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
        man.rotate = True
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.vel:       
        man.x += man.vel 
        man.right = True # helps identify which direction the player faces in when jumping, and the direction that the projectiles would go
        man.left = False  
        man.standing = False # not standing still, not facing the player
    else: 
        man.standing = True # we know if the player/man is/was moving right/left --> direction 
        man.walkCount = 0         
    if not(man.isJump): # no double jump   
        if keys[pygame.K_UP]:
            man.isJump = True # The player/man IS JUMPING   
            man.right = False 
            man.left = False
            man.walkCount = 0
    else: 
        if man.jumpCount >= -10:
            neg = 1
            if man.jumpCount < 0:
                neg = -1
            y -= (man.jumpCount ** 2) * 0.5 * neg# or: /2
            man.jumpCount -= 1 # slowly move down in jump // decrement
        else: # jump has concluded
            man.isJump = False
            man.jumpCount = 10 
    redrawGameWindow()                       

pygame.quit()       

"""
Backups/Commits
Ep 3/4 Interval: https://github.com/IrisDroidology/python-learning/commit/ef7ceb5c1d8cf08b2520993cf646c43e646523b5
"""
