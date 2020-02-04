# Link: https://www.codementor.io/@ilyaas97/6-python-projects-for-beginners-yn3va03fs --> // This code is my own, the idea came from this link
import random

for x in range(20):
    value = random.randint(1,21)
print(value)  


user_guess = int(input("What do you think the number will be?: "))

if user_guess == value:
    print("Well Done! Reload to play again")
else: 
    print("Bad luck! Reload to try again")    
