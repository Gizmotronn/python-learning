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
x = 50 # x position of character
y = 400 # remembering that the coords start from the top left of the screen in pygame /#/  can change
width = 40
height = 60
vel = 5 # speed of character --> how fast it moves
# Character Jump
isJump = False # indicates if character is jumping
jumpCount = 10

left = False
right = False
walkCount = 0 # How many steps we had

def redrawGameWindow():
    global walkCount # Global allows it to be seen anywhere

    win.blit(bg, (0,0))  
    
    if walkCount + 1 >= 27: # frame rate 
        walkCount = 0

    if left:
        win.blit(walkLeft[walkCount//3], char, (x,y))
        walkCount += 1
    elif right: 
        win.blit(walkRight[walkCount//3], char, (x,y))      # integer remainder
        walkCount += 1
    else: 
        win.blit(char, (x,y))                 
    pygame.display.update()   

# Main Game loop
run = True
while run == True:
    clock.tick(27) # FPS Set to 27

    for event in pygame.event.get(): #makes use of the module's event get feature 
        if event.type == pygame.QUIT: # if the player closes the game
            run = False # set the main game loop to false // Boolean

    keys = pygame.key.get_pressed() # makes use of the module's ability to detect the key that the player presses down on. // Pygame can also look at mouse movement

    if keys[pygame.K_LEFT] and x > vel: # left arrow key    // Solving the problem with character moving off the screen
        x -= vel
        left = True
        right = False
    elif keys[pygame.K_RIGHT] and x < screenWidth - width - vel:       
        x += vel 
        right = True
        left = False  
    else: 
        right = False
        left = False
        walkCount = 0         
    if not(isJump): # no double jump   
        if keys[pygame.K_SPACE]:
            isJump = True    
            right = False
            left = False
            walkCount = 0
    else: 
        if jumpCount >= -10:
            neg = 1
            if jumpCount < 0:
                neg = -1
            y -= (jumpCount ** 2) * 0.5 * neg# or: /2
            jumpCount -= 1 # slowly move down in jump // decrement
        else: # jump has concluded
            isJump = False
            jumpCount = 10 
    redrawGameWindow()                       

pygame.quit()       