# lists are contained in square brackets ([]) and are seprated by commas
bicycles = ["trek","cannondale","redline","specialised"]
print(bicycles)
# lists are ordered numerically from the first item in the list to the last item
# the first item in the list is position 0
# this is true for most programming languages
print(bicycles[0])              # 0 calls first item in list
print(bicycles[1])              # calls second item in list
print(bicycles[2].title())      # calls third item in list and uppercase's the first letter
print(bicycles[3].upper())      # call forth item in list and uppercase's all letters
# asking for item -1 returns the last item on the list
print(bicycles[-1])

message = "My second bicycle was a " + bicycles[1].title()+"."
print(message)