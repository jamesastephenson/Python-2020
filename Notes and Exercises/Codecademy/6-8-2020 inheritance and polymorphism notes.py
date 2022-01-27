#Inheritance and Polymorphism

#Inheritance
  #if the bulk of a class's definition is useful, but we need a new distinct-
  #-case that is distinct from how the original class was used, we can-
  #-inherit from the original class
    #ie. Inheritance is like a remix
class User:
    is_admin = False
    def __init__(self, username)
    self,username = username
class Admin(User):
    is_admin = True
  #above we defined User as our base class
  #we want to create a new class that inherits from it
    #so we created the subclass Admin
  #in this example, Admin has the same Constructor as User
  #sometimes a base class is called a parent class
    #subclass can also be called a child class
class Bin:
  pass
class RecyclingBin(Bin):
  pass

#Exceptions
  #an Exception is a class that inherits from Python's Exception class
  #we can validate this with issubclass()
    #issubclass() returns True if the first argument is a subclass of the second
    #it returns false if the first class is not a subclass of the second
    #issubclass() gives a TypeError if either argument passed is not a class
issubclass(ZeroDivisionError, Exception)
#returns True
  #above we checked whether ZeroDivisionError is a subclass of Exception
    #it is, so issubclass() returns True
  #Why is it beneificial for exceptions to inherit from one another?
class KitchenException(Exception):
  """
  Exception that gets thrown when a kitchen appliance isn't working
  """
class MicrowaveException(KitchenException):
  """
  Exception for when the microwave stops working
  """
class RefrigeratorException(KitchenException):
  """
  Exception for when the refrigerator stops working
  """
  #in the above code we defined three exceptions
    #first KitchenException acts as a parent to the other specific appliance-
    #-exceptions
    #KitchenException subclasses Exception, so it behaves in the same way that-
    #-regular Exceptions Do
    #Afterward we define Microwave Exception and RefrigeratorException as-
    #-subclasses
  #since our exceptions are subclassed in this wahy, we can katch any of-
  #-KitchenException's subclasses by catching KitchenException
  #for example:
def get_food_from_fridge():
  if refrigerator.cooling == False:
    raise RefrigeratorException
  else:
    return food
def heat_food(food):
  if microwave.working == False:
    raise MicrowaveException
  else:
    microwave.cook(food)
    return food
try:
  food = get_food_from_fridge()
  food = heat_food(food)
except KitchenException:
  food = order_takeout()
  #in the above example, we attempt to retrieve food from fridge and heat in microwave
  #if either RefrigeratorException or MicrowaveException is raised, we opt-
  #-to order takeout instead
  #we catch both exceptions in our try/except block because they are both-
  #-subclasses of KitchenException
class OutOfStock(Exception):
  pass
class CandleShop:
  name = "Here's a Hot Tip: Buy Drip Candles"
  def __init__(self, stock):
    self.stock = stock
    
  def buy(self, color):
    if self.stock[color] < 1:
      raise OutOfStock
    self.stock[color] = self.stock[color] - 1
candle_shop = CandleShop({'blue': 6, 'red': 2, 'green': 0})
candle_shop.buy('blue')

#Overriding Methods
  #override - we can override a method definition to offer a new definition-
  #-for the method in our subclass
  #an overridden method is one that has a different definition from its parent class
  #What if a User class didn't have an is_admin flag but just checked if it-
  #-had permission for something based on a permissions dictionary?
  #it should look like this:
class User:
  def __init__(self, username, permissions):
    self.username = username
    self.permissions = permissions

  def has_permission_for(self, key):
    if self.permissions.get(key):
      return True
    else:
      return False
  #above we defined a class User which takes a permissions parameter in its constructor
  #let's assume permissions is a dict
    #User has a method .has_permission_for() implemented where it checks to see-
    #-if a given key is in its permissions dictionary
  #we could then define our admin user like this
class Admin(User):
  def has_permission_for(self, key):
    return True
  #here we define an ADmin class that subclasses User
    #it has all methods, attributes, and functionality that User has
    #however, if you call has_permission_for on an instance of Admin,-
    #-it won't check its permissions dictionary
      #since this User is also an admin, we just say they have full permission
class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text
#we defined an admin class
class Admin(User):
  #we overrided the edit_message method in Admin
    #this allows an Admin to edit any messages
  def edit_message(self, message, new_text):
    message.text = new_text

#Super()
  #overriding is useful, but sometimes we want to add extra logic to an existing method
  #we use the super() method to call the method from the parent class
  #super() gives us a proxy object
    #with the proxy object, we can invoke the method of an object's parent class
    #we call the required function as a method on super()

