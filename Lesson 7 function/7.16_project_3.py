def city_country(city,country):
    """Returns a city name and country"""
    return(city.title() + " is a city in " + country.title())

answer = city_country("x","y")
print(answer)
answer = city_country("london", "the united kingdom")
print(answer)
answer = city_country("paris", "france")
print(answer)

print() # blank space

def make_album(artist,album_title):
    """Dictionary on artist and album"""
    album_dictionary = {"Artist name: " : artist.title(), "Album title" : album_title.title()}
    return album_dictionary

question_message = "Name an ablum title: "
artist_message = "Now who is the artist: "

print('Enter "quit" to quit')

while True:
    title = input(question_message)
    if title == "quit":
        break

    artist = input(artist_message)
    if artist == "quit":
        break

    album_artist = make_album(artist, title)
    print(album_artist)


