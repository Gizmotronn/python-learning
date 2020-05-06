Notion notes - https://www.notion.so/gizmotron/28-Range-ebf70cc0fe154e6ea68003dd25d2b7a4

# Range Function

- Accepting a number and it returns a sequence of numbers
- Can add multiple parameters in the range function

## Lecture

[Online Courses - Anytime, Anywhere | Udemy](https://www.udemy.com/course/python-masterclass-for-beginners/learn/lecture/13270066#content)

# Code Snippets

## Describing & Defining Range Functions

```
for x in range(6): # 6 refers to how big the range should be in index
	print(x) # Outputs 0-5 (when x in range(6))
```

## Companies Snippets

### Print all companies w/ Range Function

```
companies = ["Apple", "Google", "Samsung", "Microsoft"] # list for experimentation

for i in range(len(companies)):
	print(companies[i]) # prints companies on index "i' # prints all companies in output
```

### Print companies based on index w/ Range Function

```
companies = ["Apple", "Google", "Samsung", "Microsoft"]

for y in range(1,4): # index values
	print(companies[y])
```

### Increments

```
companies = ["Apple", "Google", "Samsung", "Microsoft"]

for q in range(10,40,5): # add 5 to "q"
	print(i) # outputs: 10, 15, 20, 30, 35 - not 40 (which is the end of the range, breaks out of cycle)
```