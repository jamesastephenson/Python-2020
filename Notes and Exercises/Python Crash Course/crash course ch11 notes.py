#Testing a Function
#sample code
def get_formatted_name(first, last):
    """Generate a neatly formatted name"""
    full_name = f"{first} {last}"
    return full_name.title()

print("Enter 'q' at any time to quit.")
while True:
    first = input("\nPlease give me a first name: \n>")
    if first == "q":
        break
    last = input("Please give me a last name: \n>")
    if last == "q":
        break

    formatted_name = get_formatted_name(first, last)
    print(f"\t Neatly formatted name: {formatted_name}")
#let's say we want to add middle names to this function
    #constantly re-running the program is tedious, but we can automate testing

#Unit Tests and Test Cases
    #the unittest module from the python standard library gives testing tools
    #Unit Test - verifies that one specific aspect of a function's behavior is correct
    #Test Case - a collection of unit tests that together prove a function behaves correctly
    
    #a good test case considers all the possible kinds of input the function could-
    #-receive and includes tests to represent each of these conditions
    #Full Coverage - full range of unit tests covering all possible ways to use a function
        #aim for critical issues first, then aim for full coverage if program will see wider use

#A Passing Test
    #to write a test case, import the unittest module and the function you want to test
        #then create a class that inherets from unittest.TestCase-
        #-and write a series of methods to test different aspects of the function's behavior
    
#Here is a test case with one method that verifies if get_formatted_name()-
#-works correctly when given a first and last name
import unittest  #imort the unittest library
class NamesTestCase(unittest.TestCase):  #create a class which will contain a series of unit tests
    #it's best to call it something related to the function you're about to test
    #also good to include the word Test in the name for clarity
    #this class MUST inherit from the class unittest.TestCase so python knows how to run the tests you write
    """tests for get_formatted_name"""

    #first method tests one aspect of get_formatted_name()
    #any method that starts with "test_" will be run automatically when we run
    #within this test method, we call the function we want to test
    def test_first_last_name(self):
        """Do names like Haruki Murakami work?"""
        formatted_name = get_formatted_name("haruki", "murakami")
        #assert methods verify that a result you received matches the result you expected to receive
        #because we know we want the test name to appear in title text, we can test that
            #the second argument should be what the program outputs for this text example
        self.assertEqual(formatted_name, "Haruki Murakami")
#it is important to note that many testing frameworks import your test files before running them
    #when a file is imported, the interpreter executes the file as it's being imported
    #the if block below makes sure it's running the test case(?)
        #book explained this kind of weird, may be worth googling or asking
if __name__ == "__main__":
    unittest.main()

