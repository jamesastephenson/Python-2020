#create a Menu class
class Menu:
  #give Menu a constructor with our 5 parameters
  def __init__(self, name, items, start_time, end_time):
    #assign all of our paremeters
    self.name = name
    self.items = items
    self.start_time = start_time
    self.end_time = end_time

  #give Menu a string repr method that will tell you the name of the menu. Also indicate when menu is available
  def __repr__(self):
    #returning a concatenated string to read out our string message
    #note: num values converted to str
    #note 2: do not need to restate arguments because they're already handled by the parent class
    return self.name + ' is available from ' + str(self.start_time) + ' to ' + str(self.end_time)

    #give Menu a calculate bill method that returns the total price of a purchase of all items in purchased_items variable
  def calculate_bill(self, purchased_items):
    total_bill = 0
    #iterate through list and add to total_bill
    for item in purchased_items:
      #quick logic statement in case they pass an item not on the menu
      if item in self.items:
        #self.items[item] syntax is used because of dictionary access
        total_bill += self.items[item]
    return total_bill
    
#storing a brunch items as a variable for easier access
brunch_items = {
  'pancakes': 7.50, 'waffles': 9.00, 'burger': 11.00, 'home fries': 4.50, 'coffee': 1.50, 'espresso': 3.00, 'tea': 1.00, 'mimosa': 10.50, 'orange juice': 3.50
}
#we create a brunch_menu object and then pass in info as arguments
#note: start and end time are in military time to keep them as integers
#note2: brunch_items uses the dictionary we defined previously
brunch_menu = Menu('Brunch', brunch_items, 1100, 1600)
#print(brunch_menu.name)  (test print)

#creating second menu item, early_bird
#store early_bird_items dict as a variable for easier access
early_bird_items = {
  'salumeria plate': 8.00, 'salad and breadsticks (serves 2, no refills)': 14.00, 'pizza with quattro formaggi': 9.00, 'duck ragu': 17.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 1.50, 'espresso': 3.00,
}
early_bird_menu = Menu('Early Bird', early_bird_items, 1500, 1800)
#print(early_bird_menu.name)  (test print)

#same as previous two examples
dinner_items = {
  'crostini with eggplant caponata': 13.00, 'ceaser salad': 16.00, 'pizza with quattro formaggi': 11.00, 'duck ragu': 19.50, 'mushroom ravioli (vegan)': 13.50, 'coffee': 2.00, 'espresso': 3.00,
}
dinner_menu = Menu('Dinner', dinner_items, 1700, 2300)
#print(dinner_menu.end_time)   (test print)

#using class to make a kids menu as well
kids_menu_items = {
  'chicken nuggets': 6.50, 'fusilli with wild mushrooms': 12.00, 'apple juice': 3.00
}
kids_menu = Menu('Kids Menu', kids_menu_items, 1100, 2100)

#print(brunch_menu)   test print

#print(brunch_menu.calculate_bill(['pancakes', 'home fries', 'coffee']))  test print for calculate_bill()

#print(early_bird_menu.calculate_bill(['salumeria plate', 'mushroom ravioli (vegan)']))  test print for calculate_bill()

#create a Franchise class
class Franchise:
  #takes the address and a list of menus
  def __init__(self, address, menus):
    #assign all parameters
    self.address = address
    self.menus = menus

  #create a string representation that says the location address
  def __repr__(self):
    return 'This location\'s address is ' + self.address
  
  #create a method that takes a time parameter and returns a list of available Menu objects
  def available_menus(self, time):
    #defining an empty list we can append to
    available_menu = [] 
    #iterate through self.menus
    for menu in self.menus:
      #set up the if statement so the menu will be apended if it is between the start and end times
      if time >= menu.start_time and time <= menu.end_time:
        available_menu.append(menu)
    return available_menu

#create our first two franchises using the Franchise class. notice that the second argument is a list of the menus
flagship_store = Franchise('1232 West End Road', [brunch_menu, early_bird_menu, dinner_menu, kids_menu])
new_installment = Franchise('12 East Mulberry Street', [brunch_menu, early_bird_menu, dinner_menu, kids_menu])

#print(flagship_store.available_menus(1200))  print statement testing available_menus method

#print(flagship_store.available_menus(1700))  print statement testing available_menus method

#define a Business class
class Business:
  #business should take a name and a list of franchises
  def __init__(self, name, franchises):
    #assign all parameters
    self.name = name
    self.franchises = franchises

business_1 = Business('Basta Fazoolin\' with my Heart', [flagship_store, new_installment])

#save new menu to a variable for easy access
arepas_menu = {
  'arepa pabellon': 7.00, 'pernil arepa': 8.50, 'guayanes arepa': 8.00, 'jamon arepa': 7.50
}
#define a franchise variable for Take a' Arepa (new restaurant). Use our Franchise class from before
arepas_place = Franchise('189 Fitzgerald Avenue', arepas_menu)
#now use the business class for Take a' Arepa
business_2 = Business('Take a\' Arepa', [arepas_place])

#COMPLETE
