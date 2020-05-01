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



# Recursion

[`Course Link`](https://www.udemy.com/course/python-masterclass-for-beginners/learn/lecture/13270196#content)



### Factorial Function

* f(n) = n * n-1 * n-2
* f(1) = 1  * 1! = 1
* f(2) = 2 * 1!
* f(3) = 3 * 2!  /// = 3 * f(2)

```python
def factorial(n):
    if n == 1:
        return 1 # ends function/algorithm & returns 1
    else:
        return n * factorial(n-1)

print(factorial(4))    # can use any int/float // Prints 24 = 4 * 3!
    
'''
* f(n) = n * n-1 * n-2
* f(1) = 1  * 1! = 1
* f(2) = 2 * 1!
* f(3) = 3 * 2!  /// = 3 * f(2)
'''    
```

