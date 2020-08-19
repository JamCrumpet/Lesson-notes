# counting to twenty
print(list(range(1,21)))

one_million = list(range(1,1000001))

#making a list from one to one million
# for x in one_million:
   # print(x)
# delete # to run code

# summing a million
# using the one million list:
# use min() and max()
print(min(one_million))
print(max(one_million))
# find the sum of a million numbers
print(sum(one_million))

# use range()  to find the odd numbers from 1 to 20
odd_numbers = list(range(1,20,2))
print(odd_numbers)

# make a list of the multiples of 3 from 3 to 30 using a for loop
threes = list(range(3,31,3))
for x in threes:
    print(x)

print(" ") # new line
# make a list of the first 10 cubes use use a for loop to print out hte value of each cube
cubes = []
for x in range(1,11):
    cube = x**3
    cubes.append(cube)
for cube in cubes:
    print(cube)