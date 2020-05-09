I'm going back to the fourth tutorial in the intro to pygame series (may have to catch up on Python as well soon). The reason for that is simple: I don't fully understand/remember the reasons for going OO (object oriented /programming) and what we do to do so, and how it works. I'll send my notes in here.

We can also see commits in https://github.com/Gizmotronn/python-learning/tree/master/Applets/TWT that reference https://github.com/Gizmotronn/python-learning/issues/22

* Everything you can do OO, you can do non-OO

https://www.youtube.com/watch?v=v_Jp11xqCzg&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt

Characteristics of our character (before OOP):

```python
x = 50 # x position of character
y = 400 # y position of character
width = 64 # width of character
height = 64 # heigh of character
vel = 5 # velocity of character in terms of pixels // He moves this many pixels per "step" or frame/
isJump = False # a variable that helps identify when the player is jumping; / this helps with doublejump (prevention), as well as other things
left = False
right = False 
walkCount = 0
```

## Create a player class:

```python
class player(object):
    def __init__(self) # initialisation function
```



# OOP Tutorial

## Tutorial 1

https://www.youtube.com/watch?v=v_Jp11xqCzg&list=PLzMcBGfZo4-l1MqB1zoYfqzlj_HH-ZzXt

```python
variable1 = 5 # integer variable, value = 5
variable2 = "10" # string variable, value = "10" (not a number)
variable2Number = int(variable2) # converting the string (or other variable type) to an integer
variable1String = str(variable1) # converting the integer (or other variable type) to a string

print(type(variable1)) # prints the type of variable that "variable1" is
>>> <class 'int'> # it says it's an integer variable
print(type(variable2))
>>> <class 'str'>
```

**Class**

* Whenever a new object (variable, for example) is created in python, it automatically creates an *instance* of that object
* In the code block above, it could be read that `variable1` is equal to `an instance of the int class; and its value is 5`.  

**Python Modules & Classes**

Turtle module:

```python
import turtle # imports the turtle (draw) module/library
square = turtle.Turtle() # initialises the turtle module, // Creating a new instance of the turtle object

# Turtle module functions
```

* In the `turtle` object, there is a class/method named *"Turtle"* 
* () --> constructor (creating a new turtle object, naming it square)

### Defining functions

```python
x = 1 # a variable called x / type: int / value: 1
def func(x): # defining a function
    return x + 1 # what is inside the functiuon
print(func(5)) # ^^ // value: 6 (adds 1 to 5)

# String functions
# Capitalization
xx = "fifty"
print(xx.upper()) # Fifty
# .upper() doesn't work unless the variable type: string 
# Replacing stuff in strings
print(xx.replace('i', 'j'))
```

* Methods can return values, too



## Tutorial 2 --> Creating Classes

Creating a new class/data type

```python
class Dog(object): # New class (dog), inherits from "object"
    def __init__(self, name, age, weight): # initializes the function/class / def = method /(things you call in the class)
		self.name = name  # creating an attribute
        self.age = age
        self.li = [1,3,4] # creating a list
        self.weight = weight
        #pass
        # print("You made a dog!") # everytime an object(dog) is created, this is printed (initialized)
    
    def speak(self):
        #pass
        print("Hi I am ", self.name, ' and I am ', self.age, ' years old.')
        
    def change_age(self, age):
        self.age = age
      
    def add_weight(self, weight):
        self.weight = weight
    
# Creating an object
myObject = Dog()
myObject = Dog("R2D2", 45) # everytime we create the [game]object(dog), we have to give it a name ^^
myObject.speak() 
myObject.change_age(5) # changes his/her/its age to "5"
myObject.add_weight(90) # in kilograms (kg)
```

* Attributes = variables, belong to a certain object
* ^^ Name is a parameter/attribute  
* `Self` always needs to be there

When we call `self.name`, the variable `name` is equal to whatever we put in the object (`myObject = Dog(WHATWEPUTINHERE)`)

* We could also use input variables for this!

I also need to figure out how old R2-D2 was!

* The `speak` function prints the values to the console



If we just want to know what the `age` (for example) is, we can:

```python
print(myObject.age) # was 45, now 5
```

* We are therefore able to access the attributes of an object, just by calling it



## Tutorial 3 --> Inheritance

We're modifying the above script, removing some stuff:

```python
class Dog(object): # New class (dog), inherits from "object"
    def __init__(self, name, age): # initializes the function/class / def = method /(things you call in the class)
		self.name = name  # creating an attribute
        self.age = age
    
    def speak(self):
        #pass
        print("Hi I am ", self.name, ' and I am ', self.age, ' years old.')
      
class Cat(object): 
        def __init__(self, name, age, color): # initializes the function/class / def = method /(things you call in the class)
        self.color = color
        self.name = name
        self.age = age
    
    def speak(self):
        #pass
        print("Hi I am ", self.name, ' and I am ', self.age, ' years old.')
```

* Inheritance --> to avoid copy and pasting, but also be able to quickly create new objects

```python
class Cat(Dog):
    def __init__(self, name, age, color)
    super().__init__(name, age)
    self.color = color
    
myCat = Cat('myCat', 2, 'blue')
myCat.speak()
```

* Parent class (`Dog`), & Derived class (`Cat`)
* `Cat` inherits from `Dog`
* Derived classes inherit all the functions and methods from their parent class
* `super().__init__()` = automatically adds self
  * `self.color` still needed to be added, as that attribute wasn't part of the `Dog` object



Changing methods in child/derived objects:

```python
	# Dog object: method/functions
    >>>...
    
    def talk(self):
        print("Bark!")
    
class Cat(Dog):
    ....
    def talk(self):
        print("Meow!")
        
myCat = Cat('myCat', 2, 'blue')
myCat.talk() # "Meow!"
myDog.talk() # "Bark!"
```

(Overriding) ^^ 

You can also set values for the attributes/variables in the object:

```python
class Cat(object): 
        def __init__(self, name, age, color): # initializes the function/class / def = method /(things you call in the class)
		self.name = 'name'  # 
        self.color = 'NoColour'
```



```python
class Vehicle(): # doesn't need the "object" in the brackets on this line
    def __init__(self, price, gas, color):
		self.price = price
        self.gas = gas
        self.color = color
        
	# method
    def fillUpTank():
        self.gas = 100 # max fuel/gas in tank
	def EmptyTank():
        self.gas = 0
    def gasLeft():
        return self.gas
    
class Car(Vehicle):
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color, speed)
        self.speed = speed
        
    def beep(self):
        print("Beep meep!')
              
class Truck(Vehicle):
    def __init__(self, price, gas, color, tires):
        super().__init__(price, gas, color, tires)
		self.tires = tires
	
	def beep(self):
        print("Loud beep!")
```

* In this way, new methods/functions can be defined for any type of object (whether child or parent)
* You can also inherit from a child object

