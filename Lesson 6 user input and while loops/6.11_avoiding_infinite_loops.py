# every while loop needs a way to stop running so it won't run forever

# for example this counting loop should count from 1 to 5:
x = 1
while x <= 5:
    print(x)
    x += 1 # omitting this line causes the loop to run forever
