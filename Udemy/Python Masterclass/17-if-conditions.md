# If Conditions

## Defining "if" conditions

```python
biggerNumber1 = 10
smallerNumber1 = 5


if smallerNumber1 < biggerNumber1:
    print("It worked") # This output does print
```

* The indentation for `print("It worked")` is used to "show the computer" that this line only proceeds *if* the above line (which is the if statement) is true

```python
biggerNumber1 = 10
smallerNumber2 = 11


if smallerNumber2 < biggerNumber2:
    print("It worked") # This output does not print
```

* As seen in this code snippet, the variable called "smallerNumber2" is actually bigger than "biggerNumber1", and the program realises this

* The line `print("It worked")` does not run, as the above statement (which is currently not true) needs to be true for the lines below it (that are indented) to run

```python
biggerNumber2 = 12
smallerNumber2 = 11


if smallerNumber2 > biggerNumber2: # true
    print("It did not work") # no output
print("End Program") # output
```

* As seen in this code snippet, the 6th line *does* run, as it is not indented. The only lines that are affected by a conditional statement are those **indented directly below the condition statement**

* If there is no indented line immediately after a conditional statement, an error occurs:

* 

* `File "C\Users\........" & python "c://Users........conditions.py" [line break] File "..."`

* `Indentation error: expected an indent block` 


