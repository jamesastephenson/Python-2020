#6-1
person_dictionary = {
    "first name": "Michael",
    "last name": "Gardiner",
    "age": "28",
    "city": "Buffalo"
    }
print(person_dictionary)

#6-2
fav_numbers = {
    "John": "34",
    "Jack": "1",
    "Jenn": "67",
    "Joe": "134",
    "Joelle": "12345"
    }
#set up a loop to go through each key:value pair
for item in fav_numbers:
    #item refers to the key here
    #fav_numbers[item] uses that key in the loop to access the value
    #": " formats the colon and space in for when it is printed
    print(item + ": " + fav_numbers[item])

#6-3
glossary = {
    "float": "a decimal number in a program",
    "variable": "an assigned object that can be used",
    "loop": "an automated format that will iterate through each item in a list",
    "if statement": "a logic statement that acts if a statement is true or false",
    "boolean": "a true or false value in python"
    }
for item in glossary:
    print(item + " - " + glossary[item])


#6-4
glossary_2 = {
    "float": "a decimal number in a program",
    "variable": "an assigned object that can be used",
    "loop": "an automated format that will iterate through each item in a list",
    "if statement": "a logic statement that acts if a statement is true or false",
    "boolean": "a true or false value in python"
    }
#if using the "for key, value" syntax, remember to use .items() on the dictionary
#for just keys you can use .keys() on the dictionary
#for just values you can use .values() on the dictionary
for key, value in glossary_2.items():
    print(f"{key} - {value}")

#6-5
rivers = {
    "Nile": "Egypt",
    "Mississippi": "America",
    "Ganges": "India"
    }

for key, value in rivers.items():
    print(f"The {key} river is in {value}")

for key in rivers.keys():
    print(key)

for value in rivers.values():
    print(value)

#6-6
favorite_languages = {
    "Jen": "Python",
    "Sarah": "C",
    "Edward": "Ruby",
    "Phil": "Python"
    }
person_list = ["Jen", "Jeff", "Sarah", "Geoff"]

for person in person_list:
    if person in favorite_languages.keys():
        print(f"Hello {person}, thank you for taking our survey!")
    else:
        print(f"Hello {person}, you should take our survey!")

#6-7
person_dictionary_2 = {
    "first name": "James",
    "last name": "Stephenson",
    "age": "25",
    "city": "San Marcos"
    }
person_dictionary_3 = {
    "first name": "Anime",
    "last name": "Jones",
    "age": "30",
    "city": "Hell"
    }

people = [person_dictionary, person_dictionary_2, person_dictionary_3]

for person in people:
    for key, value in person.items():
        print(f"{key}: {value}")
    print("")

#6-8
pet1 = {"name": "dixie", "species": "dog", "owner\'s name": "spec"}
pet2 = {"name": "birdie", "species": "bird", "owner\'s name": "birdworth"}
pets = [pet1, pet2]

for pet in pets:
    for key, value in pet.items():
        print(f"{key} - {value}")
    print("")

#6-9
favorite_places = {
    "James": "Japan",
    "Devin": "California",
    "Mike": "Toronto"
    }

for name, place in favorite_places.items():
    print(f"Name: {name} \nFavorite Place: {place}")
print("")

#6-10
fav_numbers_2 = {
    "John": ["34", "12"],
    "Jack": ["1", "12"],
    "Jenn": ["67", "12"],
    "Joe": ["134", "12"],
    "Joelle": ["12345", "12"]
    }
for key, numlist in fav_numbers_2.items():
    print(f"{key}\'s favorite numbers are: ")
    for num in numlist:
        print(num)

print("")

#6-11
cities = {
    "Danport": ["America", "12000", "It is a made up city that is not real"],
    "Waveport": ["Emgland", "40000", "This also is not a real city"],
    "Dictionaryville": ["America", "0", "Ghost Town"]
    }

for city, info in cities.items():
    print(f"Info about {city}:")
    for detail in info:
        print(detail)
