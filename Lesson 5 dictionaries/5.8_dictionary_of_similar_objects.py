# previous examples where about storing different types of information about one object
# dictionaries can one kind of information about many objects

# for example you many want to poll people on their favourite programming language
# this information is stored as following

favourite_languages = {
    "jen" : "python",
    "sarah" : "c" ,
    "edward" : "ruby" ,
    "phil" : "pyhon" ,
    }
print(favourite_languages)

# the dictionary can be use to look up the person and see their answer
print("sarah's favourite language is " +
      favourite_languages["sarah"].title() +
      ".")