import numpy as np

a = np.array([[0 ,1 ,2 ,3 ,4 ,5],
              [10,11,12,13,14,15],
              [20,21,22,23,24,25],
              [30,31,32,33,34,35],
              [40,41,42,43,44,45],
              [50,51,52,53,54,55]])
print(a)
print("\nArray Slicing:")
print("\na[0,3:5] = ", a[0,3:5]) # slices row 0 columns 3 to 5
print("\na[4:,4:] = ", a[4:,4:]) # slicing rows and columns 4+
print("\na[:,2] = ", a[:,2]) # single colon means everything along that dimension
print("\na[2::2, ::2] = ", a[2::2, ::2]) #

b = np.arange(25).reshape(5,5)
print("\nb equals")
print(b)

print("Excersies:")
print(b[4,:])
print(b[:,1::2]) # ::2 selects every 2nd column, 1:: chooses starting index
print(b[1::2,:4:2]) #

print("demo")
print(a)
print(a[ :-2 ,1:-1])
print(a[2:   ,1:-1] )
print(a[1:-1 , :-2])
print(a[1:-1 ,2:  ])
print()