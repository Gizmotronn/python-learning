# Functions in Python - 1

[`Course Link`](https://www.udemy.com/course/python-masterclass-for-beginners/learn/lecture/13270186#content)



### Defining & Calling Functions 

```python
# Define Function
def myFunction():
    # insert function instructions here
    print("Function Called")
    
# Calling function
myFunction() # this can be done multiple times in one script
```



### Function Examples

```python
def myFunction(x):
    print("Function called " + x)
    
myFunction("1") # prints "Function Called 1"    // Prints the value defined by x in this line
```



### Default values in functions

```python
def myFunction(x = "0"): # default value for x = 0 (int)
    print("Function Called " + x)
    
myFunction()
# Overriding the function
myFunction(1)

"""
>>>
Function called 0
Function called 1
"""
```





# Functions in Python - 2

[`Course Link`](https://www.udemy.com/course/python-masterclass-for-beginners/learn/lecture/13339762#content)



### Out/Return Functions

```python
def myFunction():
    print("Function 1")
    
def outFunction():
    return 10

print(outFunction) # outputs 10 as a result of the function
```



```python
def myFunction():
    print("Function 1")
    
def outFunction(x):
    return 10 * x

print(outFunction(5)) # returns 50
```



```python
def outFunction(x):
    if x == 0:
        print("Error")
        return 1
    else:
        return 10 * x
    
print(outFunction)  
```

