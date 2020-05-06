# Creating, Opening Files in Python

https://www.udemy.com/course/python-masterclass-for-beginners/learn/lecture/13270116#overview

## Opening Files

```python
open("C:\\arbuc\games\whateves") # opening file from direct path
open("my.py", "x") # opening a file in the same folder as the current file (what we're in right now!)
```

You can open .txt or binary (img) files:

```python
variableForFile = open("pythonfileopening.txt", "xt") # x = create // t = text, b = binary

variableForFile.write("aaaa") # adds this to the text file
```

