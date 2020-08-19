# this is a simple example to show how if tests let you respond
# if you have a list a car brand they should be capitalised with .title
# this does not apply to BMW and the entire name should be capitalised
# the following code loops through the list of car names and looks for "bmw" and will print the name in uppercase

cars = ["audi", "bmw", "subaru", "toyota"]
for x in cars:
    if x == "bmw:": # if the value x is equal to BMW ...
        print(x.upper()) # ... print x as .uppercase
    else: # if the value is is not equal to BMW ...
        print(x.title()) # print x as .title
