# Break, Continue - Loops #30

Luke's Programming School (Udemy) - Python Masterclass



## Lecture info

Link: https://www.udemy.com/course/python-masterclass-for-beginners/learn/lecture/13270072#overview



## Break, continue

```python
companies = ["Samsung", "Google", "Apple", "Microsoft", "Amazon", "Facebook"]
exVariable = "Example Variable"

whileOperator = 0

while whileOperator < len(companies): # whenever this variable is less than the number of items in "companies" list
    print(companies[i]) # print one company from the list // i is the index number // i comes from whileOperator
    if companies[i] == "Amazon": # if equal to Amazon
        break # break out of cycle/loop // The below line will not happen - anything in the loop below
    whileOperator += 1 # adds 1 to the value of variable (int) "whileOperator"
    
for c in companies:
    # print("c")
    if c == "Apple": # Apple is skipped
        continue
    print(c)
    
for x in example:
    print(x)
```

