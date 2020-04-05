https://www.udemy.com/course/python-masterclass-for-beginners/learn/lecture/13270082#overview



# Defining Dictionaries

```python
# Defining Dictionaries

items = {
    "Brand" : "Apple", # Pairs in dictionaries
    "Model" : "X", # Year is key
    "Year" : 2019
}

item = {
    "Brand" : "Apple", # Pairs in dictionaries
    "Model" : "X", # Year is key
    "Year" : 2019
}

# Common Operations

temp = items["Brand"]
print(temp) # Prints apple - apple is value of the pair when the key is branch

temp = items.get("Brand")
print(temp) # same output as temp = items["Brand"]



# Assigning new values to keys
items["Year"] = 2020

# Adding new pairs to dictionaries
items["Price"] = 1099

# Deleting elements from dictionaries
del items["Year"]
print(items) 



# Printing/Outputting Dictionaries
print(items)

for x in items:
    print(x) # outputs the keys in the "items" dictionaries
    print(items[x]) # values of keys
    
for x in items.values():
    print(x)
    
for x, y in itme.items():
    print(x, y) # prints key and value // multiple variables
    
if "Brand" in item:
    print("Yes")
    
# Checking value in dictionary
if "X" in item.values():
    print("Yes")
    

```

