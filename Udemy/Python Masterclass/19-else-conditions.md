# Else Condition

```python
biggerNumber1 = 10
smallerNumber1 = -5
# see 18-if-conditions.md in this folder to find out how this works
if biggerNumber1 > smallerNumber1: 
 print("It worked") 
elif smallerNumber1 > biggerNumber1: 
 print("It didn't work") 
```

Else condition/branch:

```python
biggerNumber1 = 10
smallerNumber1 = -    

if biggerNumber1 > smallerNumber1: 
 print("It worked") 
elif smallerNumber1 == biggerNumber1:  # if both variables have equal values
 print("It didn't work") 
else:
 print("It didn't work") # If none of the above conditions are met

...
```

* `Else` can be done if we have an infinite number of `if` and `elif` conditions, or just one `if` condition

* If none of the other conditions are met, the `else` is **always** followed

* It must be placed directly at the end of the conditions block


