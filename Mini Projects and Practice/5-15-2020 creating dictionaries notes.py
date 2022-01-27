#dictionary - an unordered set of key:value pairs
#in python we can create a dictionary to store price data for example
menu - {'oatmeal': 3, 'avocado toast': 6, 'carrot juice': 5, 'blueberry muffin': 2}
#NOTE:
#1. a dictionary begins and ends with curly braces {}
#2. each item consists of a key (string) and a value (number)
#3. each key:value pair is separated by a comma
#4. it's considered good practice to put a space b/w each comma
#dictionaries give us a way to map pieces of data to each other
#they let us find values that are associated with each other

sensors =  {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}
num_cameras = {"backyard": 6,  "garage": 2, "driveway": 1}

print(sensors)

#MAKING A DICTIONARY
#in prev example we used strings, but keys can be used for numbers as well
#ie.
subtotal_to_total = {20: 24, 10: 12, 5: 6, 15: 18}
#values can be any type: strings, numbers, lists, or even another dictionary can be used
#ie.
students_in_classes = {'software design': ['Aaron', 'Delila', 'Samson'], 'cartography': ['Christopher', 'Juan', 'Marco'], 'philosophy': ['Frederica', 'Manuel']}
#the list ['Aaron', 'Delila', 'Samson'] which is the value for the key "software design" represents students in that class

#you can also mix and match key and value types. ie.
person = {'name': 'Shuri', 'age': 18, 'siblings': ['TChaka', 'Ramonda']}
translations = {'mountain': 'orod', 'bread': 'bass', 'friend': 'mellon', 'horse': 'roch'}

#INVALID KEYS
#we can have a list or a dictionary as a value of an item, but not as a key
#if we tried to, we'd get a type error because it's unhashable
#unhashable - 'list' is an object that can be changed
#dictionaries in python rely on each key having a hash value
#hash value - a specific identifier for the key
#keys must be unchangable, hashable data types (ie. numbers or strings)
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"], "Corleone": ["Sonny", "Fredo", "Michael"]}
#note: this would return an error if the list was the key in each entry

#EMPTY DICTIONARY
#a dictionary doesn't have to contain anything and can be filled later
my_empty_dictionary = {}

#ADD A KEY:
#to add a key we use this syntax:
#my_dict["new_key"] = "new_value"
#for example, if we want to add to menu from earlier
menu["cheesecake"] = 8
#example:
animals_in_zoo = {}
animals_in_zoo["zebras"] = 8
animals_in_zoo["monkeys"] = 12
animals_in_zoo["dinosaurs"] = 0
print(animals_in_zoo)

#ADD MULTIPLE KEYS
#to add multiple key:value pairs to a dictionary at once, we use the .update() method
#example, if we want to add to our sensors object from earlier
sensors.update({"pantry": 22, "guest room": 25, "patio":34})
#this will add all three items to the sensors dictionary
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)

#OVERWRITE VALUES
#if you add a new assignment to a key that already exists, it will overwrite that value

#LIST COMPREHENSIONS TO DICTIONARIES
#let's say we have two lists we want to combine into a dictionary
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]
#python allows you to create a dictionary using a list comprehension w/ this syntax:
students = {key:value for key, value in zip(names, heights)}
#remember the zip() command combines two lists into a zipped list of pairs
#this list comprehension:
#1. takes a pair from the zipped list of pairs from names and heights
#2. names the elements in the pair key (the one originally from names) and value (originally from heights)
#3. creates a key:value item in the students directory
#4. repeats steps 1-3 for the entire list of pairs
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]
zipped_drinks = zip(drinks, caffeine)
drinks_to_caffeine = {key:value for key, value in zipped_drinks}

#REVIEW
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine", "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]
plays = {key:value for key, value in zip(songs, playcounts)}
print(plays)
#add "Purple Haze"
plays["Purple Haze"] = 1
#replace value for "Respect"
plays["Respect"] = 94
#create "The Best Songs" dictionary with plays, and an empty one for "Sunday Feelings"
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)






                                                                                                                                         
