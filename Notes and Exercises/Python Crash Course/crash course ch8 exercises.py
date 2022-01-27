#8-1
def display_message():
    print("This function was written to display this message.")

display_message()
print("")

#8-2
def favorite_book(book_title):
    print(f"One of my favorite books is {book_title}.")

favorite_book("Norwegian Wood")
print("")

#8-3 / #8-4
def make_shirt(shirt_size="Large", shirt_text="I love Python"):
    print(f"Shirt Size: {shirt_size} \nShirt Text: {shirt_text}")

#function called with positional argument
make_shirt("Medium", "Hamburger Friend")
#function called with keyword argument
make_shirt(shirt_text = "I love keyword arguments", shirt_size = "Medium")
#function called with default values (exercise 8-4)
make_shirt()

print("")

#8-5
def describe_city(city="Tokyo",country="Japan"):
    print(f"{city} is a city in {country}")

#call with default
describe_city()
#2 calls with other cities
describe_city("Osaka")   #still uses Japan as default country value
describe_city("London", "England")

print("")

#8-6
def city_country(city, country):
    print(f"{city}, {country}")

city_country("Santiago", "Chile")
city_country("Osaka", "Japan")
city_country("Toronto", "Canada")

print("")

#8-7
def make_album(artist_name, album_title):
    album = {"Artist": artist_name, "Album Title": album_title}
    return album

album_1 = make_album("Cosmicdust", "Snow Noise Assemblage")
album_2 = make_album("My Bloody Valentine", "Loveless")
album_3 = make_album("Weezer", "Pinkerton")

print(album_1)
print(album_2)
print(album_3)
print("")

#8-8


#8-9
text_message_list = ["lmao", "lol", "I see"]

def show_messages(message_list):
    for message in message_list:
        print(message)

show_messages(text_message_list)
print("")

#8-10 / #8-11
def send_messages(message_list):
    sent_messages = []
    for message in message_list:
        print(message)
        sent_messages.append(message)
    print(sent_messages)

send_messages(text_message_list)
print("")
print(text_message_list)
print("")

#8-12
#astrisk in the parameter denotes an arbitrary number of arguments
def make_sandwich(*toppings):
    print("Your toppings:")
    for topping in toppings:
        print(topping)

make_sandwich("Lettuce")
make_sandwich("Lettuce", "Tomato")
make_sandwich("Lettuce", "Tomato", "Bacon")

print("")

#8-13
def build_profile(first, last, **user_info):
    user_info["first_name"] = first
    user_info["last_name"] = last
    return user_info

user_profile = build_profile("albert", "einstein", location="princeton", field="physics")
print(user_profile)

user_profile_2 = build_profile("james", "stephenson", location="san marcos", field="computer")
print(user_profile_2)

print("")

#8-14
def make_car(company, model, color, year):
    made_car = {}
    made_car["company"] = company
    made_car["model"] = model
    made_car["color"] = color
    made_car["year"] = year
    return made_car

taurus = make_car("Ford", "Taurus", "Silver", "2008")
print(taurus)

