import numpy as np
# last thing on slices
x = np.array([0,1,2,3,4,])
print(x[-2]) # slices last two elements
x[-2:] = [-1,-2] # inset iterable of length two
print(x)
x[-2:] = 99 # or scalar value
print(x)
# [] are syntatic sugar, a = [0] = __getitem__(0)
# () call a functionl