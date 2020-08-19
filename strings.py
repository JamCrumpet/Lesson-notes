name = "john smith" # set name to equal John Smith
print(name.title()) # .title after name tell python to convert the first letter in each word to upper case
print(name.upper()) # .upper converts text to upper case
print(name.lower()) # .lower converts text to lower case

# combining strings
print("     COMBINING STRINGS")
first_name = "john"
last_name = "smith"
full_name = first_name + " " + last_name # set full_name to first_name + space + last name
print(full_name)
print("Hello, " + full_name.title() + "!")
greeting = "Hello, " + full_name.title() + "!"
print(greeting)

# adding whitespace # whitespace refers to non-visible characters such as spaces, tabs, and new line
print("     ADDING WHITESPACE")
print("Python")
print("\tPython") # \t adds a tab character to text
print("Languages:\nPython\nC\nJavaScript") # \n adds a new line
print("Languages: \n\tPython\n\tC\n\tJavaScript")

#removing whitespace
print("\t\tREMOVING WHITESPACE")
favourite_language = "Python   "
print(favourite_language+"!")
print(favourite_language.rstrip()+"!") # .rstrip removes extra spacing/whitespace from right side of text
language = "Javascript    "
language = language.rstrip()  #permanently removes whitespace by storing it into variable
print(language+"!")
new_language = "\tC\t"
print("space" + new_language+ "space")
print("space" + new_language.rstrip() + "space") # removes whitespace from right side of text
print("space" + new_language.lstrip() + "space") # removes whitespace from left side of text
print("space" + new_language.strip() + "space") # removes whitespace