person = {
    "first_name" : "john" ,
    "last_name" : "smith" ,
    "age" : 42 ,
    "city" : "london"
    }

print(person["first_name"])
print(person["last_name"])
print(person["age"])
print(person["city"])

favourite_numbers = {
    "john" : 42 ,
    "adam" : 33 ,
    "clark" : 76 ,
    "francis" : 64 ,
    }

result = favourite_numbers["john"]
print("John's favourite number is " + str(result) + ".")

result = favourite_numbers["adam"]
print("Adam's favourite number is " + str(result) + ".")

result = favourite_numbers["clark"]
print("Clark's favourite number is " + str(result) + ".")

result = favourite_numbers["francis"]
print("Francis' favourite number is " + str(result) + ".")