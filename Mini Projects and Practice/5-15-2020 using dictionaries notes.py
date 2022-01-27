#GET A KEY
#once you have a dictionary, you can access the values in it by providing the key
#in a given list
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#we can access the data in it like this
building_heights["Burj Khalifa"]
building_heights["Ping An"]
#example:
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
print(zodiac_elements["earth"])
print(zodiac_elements["fire"])

#GET AN INVALID KEY
#we will get a key error if we check for a key that isn't in the chosen dictionary
#one way to avoid this error is to check first if the key exists in the dictionary
key_to_check = "Landmark 81"
if key_to_check in building_heights:
  print(building_heights["Landmark 81"]
#this will not yield an hour because the if statement will return false
#therefore it will never try to access the key
zodiac_elements2 = {"water": ["Cancer", "Scorpio", "Pisces"], "fire": ["Aries", "Leo", "Sagittarius"], "earth": ["Taurus", "Virgo", "Capricorn"], "air":["Gemini", "Libra", "Aquarius"]}
zodiac_elements2["energy"] = "Not a Zodiac element"

#TRY/EXCEPT TO GET A KEY
#another method to check if a key is in a dictionary is to use try/except
key_to_check = "Landmark 81"
try:
  print(building_heights[key_to_check])
except KeyError:
  print("That key doesn't exist!")
#if we try to accept a key error that doesn't exist, the program will go into the except block
caffeine_level = {"espresso": 64, "chai": 40, "decaf": 0, "drip": 120, "matcha": 30}
try:
  print(caffeine_level["matcha"])
except KeyError:
  print("Unknown Caffeine Level")

#SAFELY GET A KEY
#in previous exercise, we had to add a key value pair to avoid a KeyError
  #this is not sustainable, we can't predict every key a user could attempt
#dictionaries have a .get() method to search for a value (instead of my_dict[key] method we've used previously)
#if the key you're trying to .get() doesn't exist, it will return None by default
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, "Abraj Al Bait": 601, "Ping An": 599, "Lotte World Tower": 554.5, "One World Trade": 541.3}
#this line will return 632:
building_heights.get("Shanghai Tower")
#this line will return None:
building_heights.get("My House")
#you can also specify what value to return if the key doesn't exist
#for example, we may want to provide a building height of 0 if the desired building is not in the dictionary
building_heights.get('Shanghai Tower', 0)
building_heights.get('Mt Olympus', 0)
#example:
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
tc_id = user_ids.get("teraCoder")
print(tc_id)
stack_id = user_ids.get("superSTackSmash", 100000)
print(stack_id)

#DELETE A KEY
#sometimes we want to get a key and remove it from the dictionary
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 320291: "Gift Basket", 412123: "Necklace", 298787: "Pasta Maker"}
#when we get a ticket number, we want to return the prize and remove that pair from the dictionary
#we can use .pop() to do this
#just like with .get(), we can provide a default value to return if the key does not exist in the dictionary
raffle.pop(320291, "No Prize")
raffle.pop(100000, "No Prize")
raffle.pop(872921, "No Prize")
#.pop() works to delete items from a dictionary when you know the key value
#example:
available_items = {"health potion": 10, "cake of the cure": 5, "green elixir": 20, "strength sandwich": 25, "stamina grains": 15, "power stew": 30}
health_points = 20
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)
print(available_items)
print(health_points)

#GET ALL KEYS
#sometimes we want to operate on all of the keys in a dictionary
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
#we want to get a roster of students in the class without including their grades
#we can do this with the built in list() function
list(test_scores)
#dictionaries also have a .keys() method that returns a dict_keys object
#a dict_keys object is a view object, which provides a look at the dictionary without letting the user modify anything
#the dict_keys object returned by .keys() is a set of the keys in the dictionary
#you cannot add or remove elements from a dict_keys object, but it can be used in place of a list iteration
for students in test_scores.keys():
    print(student)
#yields: "Grace" \n "Jeffrey" \n "Sylvia" \n "Pedro" \n "Martin" \n "Dina"
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, "samTheJavaMaam": 123112, "lyleLoop": 102931, "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
users = user_ids.keys()
lessons = num_exercises.keys()
print(users)
print(lessons)

#GET ALL VALUES
#dictionaries have a .values() method that returns a dict_values object with all of the values in the dictionary
#this is used just like dict_keys but for values
#it can be used in the place of a list for iteration
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], "Martin":[78, 80, 78], "Dina":[64, 60, 75]}
for score_list in test_scores.values():
  print(score_list)
#there is no built in function to get all the values as a list, but you can use:
  #list(test_scores.values())
#however for most purposes, the dict_list object will act the way you want a list to act
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}
total_exercises = 0
for exercises in num_exercises.values():
  total_exercises += exercises
print(total_exercises)

#GET ALL ITEMS
#you can get both keys and values with the .items() method
#like .keys() and .values() it returns a dict_list object
#each element of a dict_list returned by .items() is a tuple consisting of (key, value)
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, "Coca-Cola": 69.7, "Amazon": 64.8}
for company, value in biggest_brands.items():
  print(company + " has a value of " + str(value) + " billion dollars. ")
#example:
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, "Pharmacist": 58, "Physician": 40, "Lawyer": 37, "Aerospace Engineer": 9}
for key, value in pct_women_in_occupation.items():
  print("Women make up " + str(value) + " percent of " + key + "s")

#REVIEW
tarot = { 1:	"The Magician", 2:	"The High Priestess", 3:	"The Empress", 4:	"The Emperor", 5:	"The Hierophant", 6:	"The Lovers", 7:	"The Chariot", 8:	"Strength", 9:	"The Hermit", 10:	"Wheel of Fortune", 11:	"Justice", 12:	"The Hanged Man", 13:	"Death", 14:	"Temperance", 15:	"The Devil", 16:	"The Tower", 17:	"The Star", 18:	"The Moon", 19:	"The Sun", 20:	"Judgement", 21:	"The World", 22: "The Fool"}

spread = {}

spread["past"] = tarot.pop(13)
spread["present"] = tarot.pop(22)
spread["future"] = tarot.pop(10)

for key, value in spread.items():
  print("Your "+key+" is the "+value+" card. ")
