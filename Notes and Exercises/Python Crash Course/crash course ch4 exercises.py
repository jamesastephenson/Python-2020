#4-1
pizzas = ["Pepperoni", "Sausage", "Deep Dish"]

for pizza in pizzas:
    print("I love " + pizza)
print("I thoroughly enjoy pizzas.\n")

#4-2
birds = ["Vulture", "Falcon", "Eagle", "Finch", "Sparrow"]

for bird in birds:
    print("A " + bird + " is a bird.")
print("There are many types of birds. \n")

#4-3
#note: remember range stops at the end num, so you have to set it to 1 higher
counting_to_20 = list(range(1,21))
for num in counting_to_20:
    print(num)

#4-4
#commenting this out because it counts high
counting_to_one_million = list(range(1,1000000))
#for num in counting_to_one_million:
#    print(num)

#4-5
million_min = min(counting_to_one_million)
million_max = max(counting_to_one_million)
million_sum = sum(counting_to_one_million)

print(million_min)
print(million_max)
print(million_sum)

#4-6
#third argument in the range function is what you'll have the list count by
odd_num_list = list(range(1,21,2))
print(odd_num_list)

#4-7
threes_list = list(range(3,31,3))
for num in threes_list:
    print(num)

#4-8
counting_to_10 = list(range(1,11))
cubes = [num**3 for num in counting_to_10]
for cube in cubes:
    print(cube)

#4-9
comprehension_cubes = [x**3 for x in range(1,11)]
print(comprehension_cubes)

#4-10
print(birds[0:3])
print(birds[1:4])
print(birds[-3:])

#4-11
#[:] is there so we're setting it equal to the list items, and not reassigning it
friend_pizzas = pizzas[:]
pizzas.append("Detroit")
friend_pizzas.append("Pineapple")
print(pizzas)
print(friend_pizzas)

#4-12
for pizza in pizzas:
    print(pizza)

for pizza in friend_pizzas:
    print(pizza)

#14-3
buffet_menu = ("Spaghetti", "Soup", "Rice", "Tacos", "Chicken")
