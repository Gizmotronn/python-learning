import wikipedia

while True: # this is in a loop so it can be repeated
    input = input("Ok Pyda! ")    
    print(wikipedia.summary(input, sentences=2)) # For wikipedia queries