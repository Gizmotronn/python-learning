# part of 2-palingramspells.py
# Impractical Python - nostarch.com & github.com/acord-robotics & github/irisdroidology

"""Loading a text file (in this case the dictionary) as a list

Arguments:
1. Text File name (and directory path)

Exceptions:
1. IOError - if file isn't found

Returns:
1. List of all words (in this case) in a text file in lower case

"""

import sys # for error handling

def load(file):
    # Open a text file
    try:
        with open(file) as in_file:
            loaded_txt = in_file.read().strip().split('\n') # white space is removed
            loaded_txt = [x.lower() for x in loaded_txt] # lower case list
            return loaded_txt
        except IOError as e:
            print("{}\nError opening {}. Terminating program.".format(e, file), file=sys.stderr) # describes error and then uses sys to exit (line 28/line below)
            sys.exit(1) # terminates the program