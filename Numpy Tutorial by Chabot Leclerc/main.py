# Introduction to Numerical Computing with NumPy | SciPy 2019 Tutorial | Alex Chabot-Leclerc

import numpy as np

a = np.array([1,2,3,4])
print("Array:")
print(type(a))
print("\nArray Data type:")
print(type(a)) #<class 'numpy.ndarray'> # nd is number dimencional
print("\nData type:")
print(a.dtype)

print("\nNew f.array:")
f = np.array([1.2,4.2,9.1,6.2])
print(f.dtype) # float64 has floating point numbers fractional numbers

print("\n\n") # new line
print(a)
print(a[0]) # prints value at index 0 which is 1. python indexes at 0 e.g. 0,1,2,3
a[0] = 10
print(a) # changes value at index 0 from 1 to equal 10
print(a.ndim) # array a is one dimensional
print(a.shape) # a tuple that shows num of elements in each dimensions # a has 4 elements
print(a.size) # interger that represents number of elements in array
print(a+f)
print(a*f)
print(a/f)
print(a**f) # a vectorised operation # a single statement without a for loop
print(a*10)

# universal functions (aka ufuncs) # functions optimised to used on numpy arrays
print(np.sin(a)) # goes through sin value of a
print()

