import pygame # as pg //#/ Importing the pygame python module into this script
pygame.init() # Initialises pygame

win = pygame.display.set_mode((500, 500)) # uses the pygame module to create a window, called win, that is 500px*500px

pygame.display.set_caption("Pygame") # sets the window caption

# Character Attributes
x = 50 # x position of character
y = 50 # remembering that the coords start from the top left of the screen in pygame
width = 40
height = 60
vel = 5 # speed of character --> how fast it moves

# Main Game loop
run = True
while run == True:
    pygame.time.delay(100) # 100 miliseconds // 0.1 seconds

    for event in pygame.event.get(): #makes use of the module's event get feature 
        if event.type == pygame.QUIT: # if the player closes the game
            run = False # set the main game loop to false // Boolean

    keys = pygame.key.get_pressed() # makes use of the module's ability to detect the key that the player presses down on. // Pygame can also look at mouse movement

    if keys[pygame.K_LEFT]: # left arrow key    
        x -= vel
    if keys[pygame.K_RIGHT]:        
        x += vel    
    if keys[pygame.K_UP]:    
        y -= vel
    if keys[pygame.K_DOWN]:   
        y += vel

    win.fill((0, 0, 0)) # rgb so that the square moves rather than just accumulating    
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height)) # adding the character
    pygame.display.update()       

pygame.quit()       