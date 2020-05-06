# NumPy - Arrays (Intro)

Link: https://www.geeksforgeeks.org/numpy-in-python-set-1-introduction/

```python
[[ 1, 2, 3],
 [ 4, 2, 5]]
"""
Here,
rank = 2 (as it is 2-dimensional or it has 2 axes)
first dimension(axis) length = 2, second dimension has length = 3
overall shape can be expressed as: (2, 3) """
```

* Arrays are tables of elements (numbers usually)
* All of the same type
* Indexed by a tuple of positive integers



* Dimensions are called axes in NumPy
* The number of axes is called "rank"
* NumPy's array class = ndarray//alias = array



Demonstrating basic array characteristics:

```python
import numpy as np

# Creating array object
arr = np.array( [[ 1, 2, 3], # arr (array variable) is set to an array using numpy's array function
                [ 4, 2, 5]] )

# Printing type of arr object
print("Array is of type: ", type(arr))

# Printing dimensions
print("No. of dimensions: ", arr.ndim) 

# Printing shape of array 
print("Shape of array: ", arr.shape) 


# Printing size (total number of elements) of array 
print("Size of array: ", arr.size) 

# Printing type of elements in array 
print("Array stores elements of type: ", arr.dtype) 

"""Output:
Array is of type:  
No. of dimensions:  2
Shape of array:  (2, 3)
Size of array:  6
Array stores elements of type:  int64
"""
```



Stored here: [https://github.com/IrisDroidology/python-learning/blob/master/Udemy/Python%20Masterclass/numpy-arrays-intro.md](https://github.com/IrisDroidology/python-learning/blob/master/Udemy/Python Masterclass/numpy-arrays-intro.md)