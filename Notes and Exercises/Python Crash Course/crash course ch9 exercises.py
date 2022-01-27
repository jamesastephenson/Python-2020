#9-1
class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the name and cuisine type attributes"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        #added a number_served attribute with a default value of 0
        self.number_served = 0
    def describe_restaurant(self):
        """State the restaurant name and cuisine type"""
        #remember to refer to self.attribute here
            #it is calling to the initial class definition
        print(f"Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")
    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open")
    def print_number_served(self):
        print(f"Number Served: {self.number_served}")
    def set_number_served(self, new_number_served):
        self.number_served = new_number_served
    def increment_number_served(self, increment):
        self.number_served += increment

#9-2
pizza_obelisk = Restaurant("Pizza Obelisk", "Italian")
pizza_obelisk.describe_restaurant()
pizza_obelisk.open_restaurant()

print("")

salad_kingdom = Restaurant("Salad Kingdom", "Health")
salad_kingdom.describe_restaurant()
pizza_obelisk.open_restaurant()

print("")

burrito_galaxy = Restaurant("Burrito Galaxy", "Mexican")
burrito_galaxy.describe_restaurant()
burrito_galaxy.open_restaurant()

#9-3
class User:
    def __init__(self, first_name, last_name):
        """Initialize the first and last name attributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0
    def describe_user(self):
        print("Describing User")
        print(f"First Name: {self.first_name} \nLast Name: {self.last_name}")
    def greet_user(self):
        print(f"Thank you for signing in, {self.first_name}")
    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"{self.first_name}, you have {self.login_attempts} login attempts.")
    def reset_login_attempts(self):
        self.login_attempts = 0

anime_jones = User("Anime", "Jones")
anime_johnson = User("Anime", "Johnson")
rivers_cuomo = User("Rivers", "Cuomo")

anime_jones.describe_user()
print("")
anime_jones.greet_user()
print("")
anime_johnson.describe_user()
print("")
anime_johnson.greet_user()
print("")
rivers_cuomo.describe_user()
print("")
rivers_cuomo.greet_user()
print("")

#9-4
#added a number_served attribute to the Restaurant class with a default value of 0
#here I will be printing it with the default value and then changing it and reprinting
pizza_obelisk.print_number_served()
pizza_obelisk.set_number_served(500)
pizza_obelisk.print_number_served()

pizza_obelisk.increment_number_served(10)
pizza_obelisk.increment_number_served(10)
pizza_obelisk.increment_number_served(10)
pizza_obelisk.print_number_served()

print("")

#9-5
#added a login_attempts attribute to User class
#wrote a method called increment_login_attempts that increases the login attempts by 1
#wrote a method called reset_login_attempts which sets the attempt counter to 0
rivers_cuomo.increment_login_attempts()
rivers_cuomo.increment_login_attempts()
rivers_cuomo.increment_login_attempts()
rivers_cuomo.reset_login_attempts()
rivers_cuomo.increment_login_attempts()

#9-6
class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type, flavors):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.flavors = flavors
    def display_flavors(self):
        print("Flavors available at this location: ")
        #remember: when looping in a class, refer to the self. class instance
        #you tried putting "for flavor in flavors" which is invalid
        for flavor in self.flavors:
            print(flavor)

ice_cream_villa = IceCreamStand("Ice Cream Villa", "Ice Cream Stand", ["vanilla", "mint"])

ice_cream_villa.display_flavors()

#9-7
class Admin(User):
    def __init__(self, first_name, last_name, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print("Admins currently have these privileges: ")
        for privilege in self.privileges:
            print(privilege)

admin_privileges_list = ["Delete posts", "Ban users", "Verify users", "Edit posts"]

anime_supreme = Admin("Anime", "Supreme", admin_privileges_list)

anime_supreme.show_privileges()

#9-8
class Privileges(privileges):
    def __init__(self, privileges):
        self.privileges = privileges
    def show_privileges(self):
        print("Admins currently have these privileges: ")
        for privilege in self.privileges:
            print(privilege)

#to add into Admin class, you would set self.privileges = Privileges (the class, not the variable)

