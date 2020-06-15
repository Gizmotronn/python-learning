# https://codecombat.com/play/level/master-of-names?

# Your hero doesn't know the names of these enemies!
# Use the findNearestEnemy method on your new glasses.

# Assign the result of hero.findNearestEnemy() to the variable enemy1:
enemy1 = hero.findNearestEnemy()
# enemy1 now refers to the nearest enemy. Use the variable to attack!
hero.attack(enemy1)
hero.attack(enemy1)

# Now that enemy1 is defeated, calling hero.findNearestEnemy() again will result in finding the new nearest enemy.
enemy2 = hero.findNearestEnemy()
hero.attack(enemy2)
hero.attack(enemy2)

# Assign the result of hero.findNearestEnemy() to the variable enemy3:
enemy3 = hero.findNearestEnemy()

# Now attack using the enemy3 variable:
hero.attack(enemy3)
hero.attack(enemy3)
