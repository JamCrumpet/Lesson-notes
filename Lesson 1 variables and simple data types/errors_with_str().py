# age = 23
# message = "Happy " + age +"rd Birthday!"
# print(message)

# printing this message creates the following error

#Traceback (most recent call last):
#  File "C:/Users/f-dal/PycharmProjects/project_4_numbers/avoiding_erros_with_str().py", line 2, in <module>
#    message = "Happy" + age +"rd Birthday!"
#TypeError: can only concatenate str (not "int") to str

# Python sees that a variable that has an integer value
# Python knows that the variable could represent the number 23 or the character 2 and 3
# To specify the use of  using an integer as a string of character you must use the str() function

age = 23
message = "Happy " + str(age) + "rd Birthday"
print(message)