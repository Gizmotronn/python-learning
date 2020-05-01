# Else/If Condition: elif

Using else/if condition:

```python
biggerNumber1 = 10
smallerNumber1 = -5


if biggerNumber1 > smallerNumber1: # if the value of variable "biggerNumber1" is larger than the value of "smallerNumber1"
    print("It worked") # this only prints (as we saw in 17-if-conditions.md) if the above line is true (aka is satisfied)
elif smallerNumber1 > biggerNumber1: # elif creates a secondary "if" condition, where if 1 thing isn't true, maybe another is.
    print("It didn't work") # only prints if the above elif (which is basically a second if condition ^^) is true
```

* `elif` conditions can only be written *after* an if condition and its concluding actions, otherwise this error appears:
  
  `Syntax Error: Invalid Syntax`

* `Elif` only runs if the above conditions are not met/not satisfied, but if the above condition is met, it is not run

* You can define multiple `elif` conditions
