# Impractical Python Projects #2 (Starchfree Press)
# Github.com/IrisDroidology/Python-Learning

"""
# Contents
Line 11: Dictionary Files Link
Line 18: Ideas
Line   : Program Source Code
"""

"""
Dictionary Files - 
1. http://www-personal.umich.edu/~jlawler/wordlist.html, 
2. http://wordlist.aspell.net/12dicts/
"""

"""
Ideas
1. Some words that are created here could be found in our RPG (precursor (inscope.me) to the Stellarios game)
"""

import load_dictionary # python extension not needed, thes file loaded/imported is load_dictionary.py in the same directory as 2-palindromespells.py (THIS file)
word_list = load_dictionary.load("2of4brif.txt")

pali_list = []

for word in word_list:
    if len(word) > 1 and word == word[::-1]:
        pali_list.append(word)

print("\nNumber of palindromes found = {}\n".format(len(pali_list)))

# print in list format with no quotes or commas:
print(*pali_list, sep='\n')