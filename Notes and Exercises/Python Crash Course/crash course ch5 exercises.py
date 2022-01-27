#5-1
bagel = "everything"
print(bagel == "plain") #returns False
pizza = "pepperoni"
print(pizza == "pepperoni") #returns True
guitar = "les paul"
print(guitar != "telecaster") #returns True
cup = "mug"
print(cup != "mug") #returns False

#5-2
random_list = [2, 4, 6, 0, 1]
print(2 in random_list) #returns True
print(5 in random_list) #returns False
print(2 not in random_list) #returns False
print(5 not in random_list) #returns True

print(5 > 2) #returns True
print(5 < 2) #returns False

print(5 > 2 and 2 > 1) #returns True
print(5 < 2 and 2 < 1) #returns False
print(5 > 2 or 1 > 2) #returns True because one statement is true
print(2 > 5 or 1 > 2) #returns False because both statements are false

name = "Jean"
print(name.lower() == "jean") #returns True

#5-3
alien_color = "green"
if alien_color == "green":
    points = 5
    print(f"You have scored {points} points!")

#5-4
alien_color = "green"
if alien_color == "green":
    points = 5
    print(f"You have scored {points} points!")
else:
    points = 10
    print(f"You have scored {points} points!")

#5-5
alien_color = "green"
if alien_color == "green":
    points = 5
    print(f"You have scored {points} points!")
elif alien_color == "yellow":
    points = 10
    print(f"You have scored {points} points!")
elif alien_color == "red":
    points = 15
    print(f"You have scored {points} points!")

#5-6
age = 20
if age < 2:
    print("baby")
elif age < 4:
    print("toddler")
elif age < 13:
    print("kid")
elif age < 20:
    print("teenager")
elif age < 65:
    print("adult")
else:
    print("elder")

#5-7
favorite_fruits = ["orange", "lemon", "banana"]
if "orange" in favorite_fruits:
    print("Yes")
if "lemon" in favorite_fruits:
    print("Yes")
if "pear" not in favorite_fruits:
    print("I hate pears")
if "pomegranite" not in favorite_fruits:
    print("mythology")
    
#5-8
user_list = ["admin", "animejones", "supermario", "asdfghjkl", "the man"]
for user in user_list:
    if user == "admin":
        print("Hello admin, would you like to see a status report?")
    else:
        print(f"Hello {user}, thank you for logging in")

#5-9
user_list = []
if user_list:
    print("There are users")
else:
    print("We need some users")

#5-10
current_users = ["demi-fiend", "supermario", "boymanboy", "jeanvaljean", "billyocean"]
new_users = ["demi-fiend", "asdfgjkl", "javert", "supermario", "animejones"]

for user in new_users:
    if user.lower() in current_users:
        print("You need to make a new username.")
    else:
        print("That username is available")
        
#5-11
numbers_list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

for num in numbers_list:
    if num == "1":
        print(f"{num}st")
    elif num == "2":
        print(f"{num}nd")
    elif num == "3":
        print(f"{num}rd")
    else:
        print(f"{num}th")
