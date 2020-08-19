# multi dimensional arrays
import numpy as np

a = np.array([[0,1,2,3],[10,11,12,13]])

print(a)
print(a.shape) # n dim is 2 as their is two dimensions # (row,columns)
print(a.size) # 2*4 = 8 (element count
print(a.ndim) # number of dimensions
print(a[1,3]) # gets element from array a position [1,3]
a[1,3] = -1 # sets position a[1,3] to -1
print(a[1,3])
print(a[1]) # address row

print("\nSlicing arrays:")
# syntax still uses square brackets
# var[lower:upper:step]

a = np.array([10,11,12,13,14])
print("A equals:", a)
print(a[1:3]) # gets value from element 1 to element 3
print(a[:3])

print("\nOmitting indicies:")
print(a[:3]) # grab first three elements
print(a[:-2]) # grab last two elements
print(a[::2]) # grab every other element