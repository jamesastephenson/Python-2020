#Exceptions
    #programmers use special objects called exceptions to manage errors that arise during a program's execution
    #when an error occurs, it creates an exception object
        #if you write code that handles the exception, the code will continue running
        #if you don't, the program will halt and show a traceback, showing the error
    #exceptions are handled with try-except blocks
        #try-except blocks ask python to do something, but also what to do if an exception is raised

#Handling the ZeroDivisionError Exception
    #dividing by zero will mess up programs very quickly
    #we can use a try-except block to address the issue if it comes up
try:
    print(5/0)
except ZeroDivisionError:
    print("You can't divide by zero.")
    #we put the line that causes the error inside a try block
    #if the code in a try block works, python skips over the except block
        #if the code in the try block causes an error, python moves to the except block
    #if more code followed the try-except block, the program would continue because we handled the error

#Using Exceptions to Prevent Crashes
    #handling errors is especially important when programs ask users for input
        #responding to invalid input appropriately prevents the program from crashing
    #let's create a simple calculator that does only division
#print("Give me two numbers, and I'll divide them.")
#print("Enter \'q\' to quit.")
#while True:
#    first_number = input("\nFirst number: ")
#    if first_number == "q":
#        break
#    second_number = input("Second number: ")
#    if second_number == "q":
#        break
#    answer = int(first_number) / int(second_number)
#    print(answer)

    #this program does nothing to handle errors, so dividing by 0 will make it crash
    #crashing is bad and traceback errors can give attackers more info than you want
#we can make this code more error resistant by using a try-except block and an else block

print("Give me two numbers, and I'll divide them.")
print("Enter \'q\' to quit.")
while True:
    first_number = input("\nFirst number: ")
    if first_number == "q":
        break
    second_number = input("Second number: ")
    if second_number == "q":
        break
    try:
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        print("You can't divide by 0.")
    else:
        print(answer)
    #we ask python to trhy to complete the division in a try block
        #try block is the place where it may cause an error in this case
        #we anticipate the ZeroDivisionError and account for that in the except block
            #then if someone divides by 0, we can display an error message
#The try-except-else block works like this:
    #python attempts to run the code in the try block
        #the only code that should go in the try block is code that might cause an exception to be raised
    #additional code that only runs if the try block is successful goes in the else block
    #the except block tells python what to do if an error arrives in the try block

#Handling the FileNotFoundError Exceptions:
    #a common error is if a file is missing, misspelled, or doesn't exist, etc
        #this can be handled with a try-except block
#here we'll try to open a file that doesn't exist and address the error
filename = "alice.txt"
try:
    with open(filename, encoding="utf-8") as f:
        #note:using the variable f to represent the file object is a common convention
        #the encoding argument is needed when your system's default encoding doesn't match-
        #-the encoding of the file being read
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
#in this example, the code in the try block produces a FileNotFound error so python looks for-
#-an except block that matches that error
    #python then runs the code in that block

#Analyzing Text
    #using the split() function, you can break each word in a string into a list
        #that list also can be saved as an object
