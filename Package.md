# Exploration Activity 2


## Library
I utilized the numpy library in Python


## What is the numpy library in Python
NumPy is a Python library used for working with arrays.      
It also has functions for working in the domain of linear algebra, fourier transform, and matrices.



### How do you use it
The first thing is to import into Python "import numpy". You could also use it as a shorthand such as "import numpy as np".   
The basic functionality of numpy is array creation and manipulation.   
I will go through some basic ways to work with arrays with numpy.    

1. Creating an array: arr = np.array([1, 2, 3, 4, 5]) / np.array((1, 2, 3, 4, 5))
2. Creating multi-dimensional array = np.array([1, 2, 3, 4], ndmin=(number of dimensions))
3. Checking dimension : array.ndim 
4. Array indexing: array[index position] (starts from 0) (negative indexing starts from the end of array)
5. Array slicing: array[start:end] or array[start:end:step]
6. Copying an array: x = array.copy()
7. Viewing an array: x = array.view()
8. Shape of an array: array.shape
9. Reshaping an array: arr.reshape(row, column)
10. Joining arrays: x = np.concatenate((arr1, arr2)) / np.stack((arr1, arr2), axis=1)
11. Splitting arrays: x = np.array_split(array, parts)
12. Searching arrays: x = np.where(array == value)
13. Sorting arrays: x = np.sort(array)

Numpy has numerous other functionalities but I have chosen to cover basic array manipulation for this section


## When was it created
NumPy was created in 2005 by Travis Oliphant. It is an open source project and you can use it freely.    
NumPy stands for Numerical Python.


## Why did I select this library
While working with Python, I noticed Python didn't have basic array functionalities like other programming languages like Java.   
Upon research, I found out about this library that adds array functionality to Python.       
I wanted to see how it works in comparison to the array functionality in other languages.   


## How did learning the library affect my learning of Python
It made me realize that there are easier ways to do certain things in Python as numpy comes with a lot of in-built functionality.


## Overall experience 
I would recommend this library to someone especially if they are working with large datasets.    
They could benefit from the built-in functions of numpy.   
I would keep using this library, I enjoyed creating a matrix calculator using the numpy functionalities.     
I feel the in-built functions are better than other languages provide with their arrays. 





