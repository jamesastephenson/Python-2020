#chapter 9 notes

#creating the dog class
#we define the class Dog
    #no parentheses because we're creating the class from scratch
class Dog:
    #docstring describing what the class does
    """A simple attempt to model a dog."""

    #a function that's part of a class is called a Method
    #the __init__ method is a special method that runs automatically when-
    #-we create a new instance based on the Dog class
    
    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")
        
