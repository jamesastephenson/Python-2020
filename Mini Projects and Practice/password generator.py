#Password Generator
#This program will give a randomized password containing 2 upper case letters,-
#-2 lower case letters, 2 numbers, and 2 punctuation marks
#it will then shuffle the password

#This exercise will test usage of ascii characters

#begin by importing the random library
import random

#create a function that will shuffle our password when the characters are chosen
def shuffle_password(string):
    #converts string argument to a temporary list
    temp_list = list(string)
    #uses the shuffle command in the random library on temporary list
    random.shuffle(temp_list)
    #join command makes a string from an iterable object
    #returns the shuffled result
    return "".join(temp_list)

#defining our characters as variables for modularity
#note: when defining these, we use chr() surrounding the generator to prevent a type error
#97-122 are lower case characters
lowercase_letter_1 = chr(random.randint(97, 122))
lowercase_letter_2 = chr(random.randint(97, 122))
#65-90 are upper case characters
uppercase_letter_1 = chr(random.randint(65, 90))
uppercase_letter_2 = chr(random.randint(65, 90))
#48-57 are single digit integers
number_1 = chr(random.randint(48, 57))
number_2 = chr(random.randint(48, 57))
#33-47 are a handfull of punctuation marks
punctuation_1 = chr(random.randint(33, 47))
punctuation_2 = chr(random.randint(33, 47))

#generate an unshuffled version of the password including one of each of our variables
unshuffled_password = lowercase_letter_1 + lowercase_letter_2 + uppercase_letter_1 + uppercase_letter_2 + number_1 + number_2 + punctuation_1 + punctuation_2
#use the shuffle function on our unshuffled password
shuffled_password = shuffle_password(unshuffled_password)

print("Your randomized password is: " + shuffled_password)
