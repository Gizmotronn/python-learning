# From https://www.thepythoncode.com/article/access-wikipedia-python
import wikipedia # imports wikipedia pip/py module // install python and type into command prompt "pip3 install wikipedia"

# Print what Wikipedia is
print(wikipedia.summary("Python programming language")) # this uses the wikipedia pipy module to print the start/summary of the wikipedia page for the "Python Programming Language"

"""
Output:
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace. Its language constructs and object-oriented approach aim to help programmers write clear, logical code for small and large-scale projects.Python is dynamically typed and garbage-collected. It supports multiple programming paradigms, including procedural, object-oriented, and  functional programming. Python is often described as a "batteries included" language due to its comprehensive standard library.Python was conceived in the late 1980s as a successor to the ABC language. Python 2.0, released in 2000, introduced features like list comprehensions and a garbage collection system capable of collecting reference cycles. Python 3.0, released in 2008, was a major revision of the language that is not completely backward-compatible, and much Python 2 code does not run unmodified on Python 3.
The Python 2 language, i.e. Python 2.7.x, was officially discontinued on January 1, 2020 (first planned for 2015) after which security patches and other improvements will not be released for it. With Python 2's end-of-life, only  Python 3.5.x and later are supported.
Python interpreters are available for many operating systems. A global community of programmers develops and maintains CPython, an open source reference implementation. A non-profit organization, the Python Software Foundation, manages and directs resources for Python and CPython development.
"""


# Only 2 sentence summary
print(wikipedia.summary("Python programming", sentences=2))

"""
Output:
Python is an interpreted, high-level, general-purpose programming language. Created by Guido van Rossum and first released in 1991, Python's design philosophy emphasizes code readability with its notable use of significant whitespace.
"""


# Searching for a term in wikipedia search
result = wikipedia.search("Neural networks")
print(result)

"""
Output:
['Neural network', 'Artificial neural network', 'Convolutional neural network', 'Recurrent neural network', 'Rectifier (neural networks)', 'Feedforward neural network', 'Spiking neural network', 'Dropout (neural networks)', 'Quantum neural network', 'Neural circuit']
"""

# Get the whole page for first (initial) result of search
page = wikipedia.page(result[0])
# Crawling the title
title = page.title
# Get the categories of the page
categories = page.categories
# Extract text after removing all HTML tags
content = page.content # done automatically
# Get all links from page
links = page.links
# References from page
references = page.references
# Summary from page
summary = page.summary

# Printing them all out:
print("Page content:\n", content, "\n")
print("Page title:", title, "\n")
print("Categories:", categories, "\n")
print("Links:", links, "\n")
print("References:", references, "\n")
print("Summary:", summary, "\n")