import pygame # as pg //#/ Importing the pygame python module into this script
pygame.init() # Initialises pygame

win = pygame.display.set_mode((500, 500)) # uses the pygame module to create a window, called win, that is 500px*500px

pygame.display.set_caption("Pygame") # sets the window caption

# Loading images/sprites
# This goes outside the while loop, near the top of the program
walkRight = [pygame.image.load('R1.png'), pygame.image.load('R2.png'), pygame.image.load('R3.png'), pygame.image.load('R4.png'), pygame.image.load('R5.png'), pygame.image.load('R6.png'), pygame.image.load('R7.png'), pygame.image.load('R8.png'), pygame.image.load('R9.png')] # list
walkLeft = [pygame.image.load('L1.png'), pygame.image.load('L2.png'), pygame.image.load('L3.png'), pygame.image.load('L4.png'), pygame.image.load('L5.png'), pygame.image.load('L6.png'), pygame.image.load('L7.png'), pygame.image.load('L8.png'), pygame.image.load('L9.png')] # You COULD flip the images, but that's not what's happening here :)
bg = pygame.image.load('bg.jpg')
char = pygame.image.load('standing.png')

# Clock
clock = pygame.time.Clock()

screenWidth = 500
screenHeight = 480 

# Character Attributes
class player(object):
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.jumpCount = 10
        self.left = False
        self.right = False
        self.walkCount = 0 # See end of document to see what it looked like without object oriented
        self.standing = True # standing still

    def draw(self,win): # argument of the window
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

class projectile(object):
    def __init__(self,x,y,radius,color,facing):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing = facing
        self.vel = 8 * facing # determines whether the projectile will move left or right

    def draw(win):
        pygame.draw.circle(win, self.color, (self.x,self.y), self.radius) # ,1 before the close bracket makes the circle not filled in    

def redrawGameWindow():
    global walkCount # Global allows it to be seen anywhere

    win.blit(bg, (0,0))  

    man.draw(win)         

    pygame.display.update()   

# Main Game loop
man = player(300, 410, 64, 64)
bullets = [] # list --> projectiles//
run = True
while run == True:
    clock.tick(27) # FPS Set to 27

    for event in pygame.event.get(): #makes use of the module's event get feature 
        if event.type == pygame.QUIT: # if the player closes the game
            run = False # set the main game loop to false // Boolean
    for bullet in bullets # for every bullet inside the "bullets"list
        if bullet.x < 500 and bullet.x > 0: # bullet not going off screen
            bullet.x += bullet.vel 
        else: # bullet is off screen
            bullets.pop(bullets.index(bullet)) # pop = remove element            

    keys = pygame.key.get_pressed() # makes use of the module's ability to detect the key that the player presses down on. // Pygame can also look at mouse movement

    if keys[pygame.K_SPACE:
        if len(bullets)

    if keys[pygame.K_LEFT] and man.x > man.vel: # left arrow key    // Solving the problem with character moving off the screen
        man.x -= man.vel
        man.left = True
        man.right = False
        man.standing = False
    elif keys[pygame.K_RIGHT] and man.x < screenWidth - man.width - man.vel:       
        man.x += man.vel 
        man.right = True
        man.left = False  
        man.standing = False # not standing still, not facing the player
    else: 
        man.standing = True # we know if the player/man is/was moving right/left --> direction 
        man.walkCount = 0         
    if not(man.isJump): # no double jump   
        if keys[pygame.K_UP]:
            man.isJump = True    
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