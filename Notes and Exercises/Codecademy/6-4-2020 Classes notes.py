#Classes

#Types
  #Python equips us with different ways to store data
  #different kinds of data are known as different types
    #ie. float and int are different types
  #we can check the type of a python variable using the type() function
a_string = 'This is a string'
an_int = 12
print(type(a_string))
    #prints '<class 'str'>'
print(type(an_int))
    #prints '<class 'int'>'
  #a variable's type determines what you can and can't do with it
  #you can't .get() something from an integer
  #you also can't add two dictionaries using +
  #operations are defined at the type level
print(type(5))
my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))

#Class
  #a class is a template for a data type
    #it describes the kind of info the class will hold and how to interact w/ it
  #define a class using the class keyword
    #it is recommended to capitalize class names to make them easy to spot
class CoolClass:
    pass
  #in the above example we created a class named CoolClass
  #we used the pass keyword in Python to indicate that the body of the class-
  #-was intentionally left blank so we don't cause an IndentationError

#Instantiation
  #a class must be instantiated, meaning we must create an instance of the class
  #instantiating a class looks a lot like calling a function
cool_instance = CoolClass()
  #above we created an object by adding parentheses to the name of the class
  #then we assigned that new instance to the variable cool_instance

#Object Oriented Programming
  #a class instance is also called an object
  #Object Oriented Programming is the pattern of defining classes and creating-
  #-objects to represent the responsibilities of a program
  #instantiation takes a class and turns it into a vunction
    #the type() function does the opposite of that
print(type(cool_instance))
    #prints "<class '__main__.CoolClass'>"
  #in Python __main__ means 'this current file we're running'

#Class Variables
  #when we want the same data to be available to every class instance,-
  #-we use a class variable
  #a class variable is a variable that's the same for every instance of the class
  #you can define a class variable by including it in the indented part of-
  #-your class definition
  #you can access all of an object's class variables with object.variable syntax
class Musician:
    title = 'Rockstar'
drummer = Musician()
print(drummer.title)
    #prints 'Rockstar'
  #above we defined the class Musician and then instantiated drummer to be-
  #-an object of type Musician
  #we then printed out the drummer's .title attribute, which is a class-
  #-variable that we defined as the string 'Rockstar'
    #if we defined another musician, they would have the same .title attribute
      #ie. guitarist = Musician()
class Grade:
  minimum_passing = 65

#Methods
  #methods are functions that are defined as part of a class
  #the first argument in a method is alwyas the object that is calling the method
  #convention recommends naming this first argument self
    #methods always have at least this one argument
  #we define methods similarly to functions, except they are indented to be-
  #-part of the class
class Dog:
    dog_time_dilation = 7

    def time_explanation(self):
        print('Dogs experience {} years for every 1 human year.'.format(self.dog_time_dilation))
pipi_pitbull = Dog()
pipi_pitbull.time_explanation()
#prints out 'Dogs experience 7 years for everyone 1 human year'
  #above we created a Dog class with a time_explanation method that takes-
  #-one argument, self, which refers to the object calling the function
  #we created a dog named pipi_pitbull and called the .time_Explanation() method-
  #-on our new object for Pipi
  #notice we didn't pass any arguments when we called .time_explanation(), but-
  #-were able to refer to self in the function body
  #when you call a method it automatically passes the object calling the method-
  #-as the first argument
class Rules:
  pass
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

#Methods with Arguments
  #methods can also take more arguments than just self
class DistanceConverter:
    kms_in_a_mile = 1.609
    def how_many_kms(self, miles):
        return miles * self.kms_in_a_mile
converter = DistanceConverter()
kms_in_5_miles = converter.how_many_kms(5)
print(kms_in_5_miles)
#prints '8.045'
  #above we defined a DistanceConverter class, instantiated it, and-
  #-used it to convert 5 miles into kilometers
  #notice again that how weven though how_many_kms takes two arguments-
  #-in its definition, we only pass miles, because self is implicitly passed
    #(and refers to the object converter)
class Circle:
  pi = 3.14
  def area(self, radius):
    #because pi is a class variable, you access it as-
    #-an attribute of the class 'Circle.pi'
    area = Circle.pi * radius ** 2
    return area
circle = Circle()
pizza_area = circle.area(6)
teaching_table_area = circle.area(18)
round_room_area = circle.area(5730)

#Constructors
  #dunder methods - methods we can define in a class that have special behavior
    #__init__ method - used to initialize a newly created object
      #called every time the class is instantiated
  #constructors - methods that are used to prepare an object being instantiated
    #note: in python normally a constructor refers to the __init__ method
    #the word "constructor" is used to describe similar features in other OOP languages
class Shouter:
    def __init__(self):
        print('HELLO?!')
shout1 = Shouter()
#prints 'HELLO?!'
shout2 = Shouter()
#prints 'HELLO?!'
  #above we created a class called Shouter
    #every time we create an instance, the program prints out a shout
  #pay attention to the instantiation syntax we use
    #we can pass parameters into the parenteses to be received by the __init__ method
class Shouter2:
    def __init__(self, phrase):
        #make sure phrase is a string
        if type(phrase) == str:
            #then shout it out
            print(phrase.upper())
shout3 = Shouter('shout')
#prints SHOUT
  #above we've updated our Shouter2 class to take the additional parameter phrase
  #when we created each of our objects, we passed an argument to the constructor
  #the constructor takes the argument of phrase and, if it's a string-
  #-prints out the all caps version of phrase
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    #the diameter=diameter statement is here to replace the {}
    print("New circle with diameter: {diameter}".format(diameter=diameter))
teaching_table = Circle(36)

#Instance Variables
  #a class is a schematic for a data type and an object is an instance of a class
  #each instance of a class can hold different types of data
    #the data held by any object is referred to as an instance variable
    #instance variables aren't shared by all instances of a class.-
    #-they're variables that are specific to the object they're attached to
  #let's say we have this class definition
class FakeDict:
  pass
  #we can instantiate two different object sfrom this class, fake_dict1 and fake_dict2
  #we can assign instance variables to these objects using the same notation-
  #-used for accessing class variables
fake_dict1 = FakeDict()
fake_dict2 = FakeDict()
fake_dict1.fake_key = "This works!"
fake_dict2.fake_key = "This too!"
# Let's join the two strings together!
working_string = "{} {}".format(fake_dict1.fake_key, fake_dict2.fake_key)
print(working_string)
# prints "This works! This too!"
#example:
class Store:
  pass
alternative_rocks = Store()
isabelles_ices = Store()
alternative_rocks.store_name = 'Alternative Rocks'
isabelles_ices.store_name = 'Isabelle\'s Ices'

#Attribute Functions
  #instance variables and class variables are both accessed similarly in python
    #they are both considered attributes of an object
    #if we attempt to access an attribute that is neither a class variable-
    #nor an instnace variable of the object, Python will give an AttributeError
class NoCustomAttributes:
    pass
attributeless = NoCustomAttributes()
try:
    attributeless.fake_attribute
except AttributeError:
    print('This text gets printed')
#prints 'This text gets printed'
  #getattr() is a python function that works like dot syntax (ie, object.attribute)-
  #-but we can supply a third argument that will be the default if the object-
  #-does not have the given attribute
  #hasattr() is a command that will return True if it has an attribute
hasattr(attributeless, 'fake_attribute')
#returns False
getatr(attributeless, 'other_fake_attribute', 800)
#returns 800, the default value
  ##above we checked if attributeless has the attribute fake_attribute
    #it doesn't, so hasattr() returned False
  #our call to getattr() returned the default value 800 instead of an error
how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]
#set up a for loop to iterate through the list
for element in how_many_s:
  #check if the element has the attribute count
  if hasattr(element, "count"):
    #then it counts the number of times 's' appears in the element
    print(element.count("s"))

#Self
  #dictionaries already store key-value pairs, so objects aren't useful for that
  #instance variables are more powerful when you can guarantee rigidity to the-
  #-data the object is holding
  #the convenience is apparent when the constructor creates the instance variables-
  #-using the arguments passed into it
#if we were creating a search engine, and wanted classes for each separate-
#-entry we could return, we'd do that like this:
class SearchEngineEntry:
    def __init__(self, url):
        self.url = url
codecademy = SearchEngineEntry('www.codecademy.com')
wikipedia = SearchEngineEntry('www.wikipedia.org')
print(codecademy.url)
#prints 'www.codecademy.com'
print(wikipedia.url)
#prints 'www.wikipedia.org'
  #since the self keyword refers to the object and not the class being called,-
  #-we can define a secure method on the SearchEngineEntry class that returns-
  #-the secure link to an entry
class SearchEngineEntry:
    secure_prefix = 'https://'
    def __init__(self, url):
        self.url = url
    def secure(self):
        return '{prefix}{site}'.format(prefix=self.secure_prefix,site=self.url)
codecademy = SearchEngineEntry('www.codecademy.com')
print(codecademy.secure())
#prints 'https://www.codecademy.com'
print(wikipedia.secure())
#prints 'https://www.wikipedia.com'
  #above we defined our secure() method to take jsut the one required argument self
  #we access both the class variable self.secure_prefix and the instance-
  #-variable self.url to return a secure URL
  #this is the strength of writing object oriented programs
    #we can write our classes to structure the data that we need
    #and we can write methods that will interact with data in a meaningful way
class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    
    self.radius = diameter / 2
    
  def circumference(self):
    #remember you have to use self.pi and self.radius
      #this is to make sure they're defined properly
    return 2 * self.pi * self.radius
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())


#Everything is an Object
  #attributes can be added to user defined objects after instantiation,-
  #-so it's possible for an object to have some attributes that are not-
  #-specifically defined in an object's constructor
  #dir() can be used to investigate an object's attributes at runtime
  #dir() is short for directory and offers an organized presentation of object attributes

class FakeDict:
  pass

fake_dict = FakeDict()
fake_dict.attribute = "Cool"

dir(fake_dict)
# Prints ['__class__', '__delattr__', '__dict__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__gt__', '__hash__', '__init__', '__init_subclass__', '__le__', '__lt__', '__module__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', '__weakref__', 'attribute']
  #this is more than we defined because python auto adds a number of attributes-
  #-to all objects that get created
  #these internal attributes are usually indicated by double underscores
    #attribute is on that list
  #python's native data types (int, float, str, etc) are all also objects
    #they have special syntax for their instantiation as we've used
    #these instances are still full blown objects
fun_list = [10, "string", {'abc': True}]

type(fun_list)
# Prints <class 'list'>

dir(fun_list)
# Prints ['__add__', '__class__', [...], 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
  #above we define a new list, we check its type, and see an instantiation of class list
  #we use dir() to expose its attributes and it gives us a lot of internal-
  #-Python dunder attributes
  #afterwards we get the usual list methods
print(dir(5))
def this_function_is_an_object(yes):
  return 'yes'
print(dir(this_function_is_an_object))

#String Representation
  #one of the first things we learn is how to print info for debugging
  #unfortunately when we print out an object we get a default representation-
  #-that seems fairly useless
class Employee():
    def __init__(self, name):
        self.name = name
argus = Employee('Argus Filch')
print(argus)
#prints "<__main__.Employee object at 0x104e88390>"
  #this default string representation gives us some info, like where the class-
  #-is defined and our computer's memory address where this object is stored
  #however thi information is not useful for debugging
#new dunder method: __repr__
  #__repr__ is a method that tell's python what we want the string representation-
  #-of the class to be
  #__repr__ can only have one parameter, self, and must return a string
class Employee():
  def __init__(self, name):
    self.name = name
  def __repr__(self):
    return self.name
argus = Employee("Argus Filch")
print(argus)
# prints "Argus Filch"
  #we implemented the __repr__ method and had it return the .name attribute
  #when we printed the object out, it simply printed the .name of the object

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)


#review
class Student:
  #constructor takes a name and year. attributes saved to .name and .year
  def __init__(self, name, year):
    #this syntax is for referring to self in the class argument
    self.name = name
    self.year = year
    #empty list for grades
    self.grades = []
  #.add_grade() method that takes the parameter grade
  def add_grade(self, grade):
    #first verifies if grade is of type Grade
      #if yes, it appends it to the Student's .grades
    if type(grade) is Grade:
      self.grades.append(grade)      
#setting a Grade class
class Grade:
  #holds the minimum_passing value. this is the constructor for Grade class
  minimum_passing = 65
  
  def __init__(self, score):
    self.score = score

#defining student names and their year, saving as variable
    #notice they're using the student class
roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)
#adding grade of 100 to pieter
pieter.add_grade(Grade(100))
