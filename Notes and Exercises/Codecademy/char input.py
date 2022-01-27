#This program has the user input their name and birthday-
#-it then says in what year they will turn 100

#input() asks user to input the assignment for the variable
name = input('Enter your name: ')
#int() is put first in this assignment so that the num is not a string
birth = int(input('Enter the year you were born: '))
#set the input varisble birth to now be a string so we can concatenate it
    #numbers must be converted to strings to be used
birth_string = str((birth + 100))
#final print statement with concatenated end string
print('Hello ' + name + ' you will be 100 years old in the year ' + birth_string)
