[Week 0: Intro to Module](https://www.notion.so/Week-0-Intro-to-Module-9af872c5d9c0455e84bd1932aaf087c6)

## Commits

- [https://github.com/IrisDroidology/python-learning/commit/b62605754f10477df4910f5f5fbf5fd63ab6e2c9](https://github.com/IrisDroidology/python-learning/commit/b62605754f10477df4910f5f5fbf5fd63ab6e2c9)

```
will put some notes on notion soon

youtube.com/watch?v=PVY46hUp2EM

Issues (before starting to program):
1. When the player stops walking, he faces outwards from the screen (school repo/physics palm/grip rule). Which way will the bullet go?

More coming soon!

Co-Authored-By: Liam Arbuckle <allianceofdroidsla@gmail.com>
```

- To solve the issue outlined above, we need to ensure that the player is always facing left or right (for this tutorial!)
- Multiple bullets/projectiles:
    - Each bullet needs to have its own velocity so we know if it's traveling left or right, as two bullets may be shot at different directions (which ultimately depends upon the velocity and its sign (+ or -))

## Projectiles

- If they collide with the wall, they disappear
- Shot from the player's hand

Creating a new class:

```python
class projectile(object):
	def __init__(self,x,y,radius,color,facing): # initializing the class and its attributes
		self.x = x
		self.y = y
		self.radius = radius
		self.color = color
		self.facing = facing
		self.vel = 8 * facing # if the facing is (-), the vel will be - and the bullet/projectile will go left

	def draw(self,win): # draw the projectile
		pygame.draw.circle(win, self.color, (self.x,self.y), self.radius) # draw the window, then chooses the colour/color, coords, and size (radius, as it's a circle-ish shape)
```

- Here we've defined the class and given it similar attributes to the player
    - `Facing` refers to the velocity and the direction it will go

**We then need to modify the player class:** 

Here's the new player class

```python
class player(object):
    def __init__(self,x,y,width,height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.vel = 5
        self.isJump = False
        self.left = False
        self.right = False
        self.walkCount = 0
        self.jumpCount = 10
        self.standing = True

    def draw(self, win):
        if self.walkCount + 1 >= 27:
            self.walkCount = 0

        if not(self.standing):
            if self.left:
                win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                self.walkCount += 1
            elif self.right:
                win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                self.walkCount +=1
        else:
            if self.right:
                win.blit(walkRight[0], (self.x, self.y))
            else:
                win.blit(walkLeft[0], (self.x, self.y)) 
```

Old player class:

```python
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

    def draw(self,win): # argument of the window
	    if self.walkCount + 1 >= 27: # frame rate 
        self.walkCount = 0

	    if left:
        win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
        self.walkCount += 1
	    elif right: 
        win.blit(walkRight[walkCount//3], (self.x,self.y))      # integer remainder
        self.walkCount += 1
	    else: 
        win.blit(char, (self.x,self.y))
```

What we did when we modified the player class:

- Modified the `player.draw` *method*
- Added another attribute of `standing` to the player:
    - `self.standing = True` in *line* *13*
- Ensure that the player is always facing left or right:

    ```python
    if not(self.standing):
                if self.left:
                    win.blit(walkLeft[self.walkCount//3], (self.x,self.y))
                    self.walkCount += 1
                elif self.right:
                    win.blit(walkRight[self.walkCount//3], (self.x,self.y))
                    self.walkCount +=1
            else:
                if self.right:
                    win.blit(walkRight[0], (self.x, self.y))
                else:
                    win.blit(walkLeft[0], (self.x, self.y))
    ```

Currently at `2:48`

[Pygame Tutorial #5 - Projectiles](https://youtube.com/watch?v=PVY46hUp2EM)

Tutoring w/ Liam & AC0/RD
