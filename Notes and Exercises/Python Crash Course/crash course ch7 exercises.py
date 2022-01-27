#7-1
car_request = input("What type of car would you like to rent? \n>")
car_request = car_request.title()
print(f"Let me see if I can find you a {car_request}")
print("")

#7-2
dinner_group_size = int(input("Hello! How many people are in your dinner group today? \n>"))
if dinner_group_size >= 8:
    print("Sorry, you\'ll have to wait for a table.")
else:
    print("We have a table ready for you.")
print("")

#7-3
user_number = int(input("Enter a number to see if it is a multiple of 10 \n>"))
if 10 % user_number == 0:
    print("Your number is a multiple of 10")
else:
    print("Your number is not a multiple of 10.")
print("")

#7-4
trigger_7_4 = True
while trigger_7_4 == True:
    pizza_topping = str(input("Please enter a pizza topping. (type \'quit\' to exit) \n>"))
    if pizza_topping == "quit":
        trigger_7_4 = False
    else:
        print(f"Ok! Adding {pizza_topping} to your pizza!")
print("")

#7-5
moviegoer_age = int(input("Hello, how old are you? \n>"))
if moviegoer_age < 3:
    print("Your ticket is free.")
elif moviegoer_age > 12:
    print("Your ticket is $15")
else:
    print("Your ticket is $10")

print("")

#7-6
#covered by previous exercises

#7-7
#commented out because it creates an infinite loop
#num = 1
#while num > 0:
    #num +=1

#7-8 / #7-9
sandwich_orders = ["chicken sandwich", "pastrami", "tuna sandwich", "roast beef sandwich"]
finished_sandwiches = []

for order in sandwich_orders:
    if order == "pastrami":
        print("Sorry, we are out of pastrami")
        #continue statement means that "pastrami" will be ignored and not be appended
        continue
    print(f"Now making your {order}")
    finished_sandwiches.append(order)
print("Completed sandwiches: ")
print(finished_sandwiches)

print("")

#7-10
trigger_7_10 = True
survey_results = []
while trigger_7_10 == True:
    dream_vacation = input("What is your dream vacation destination? (type \'quit\' when survey is complete) \n>")
    if dream_vacation == "quit":
        break
    survey_results.append(dream_vacation)
print(survey_results)
