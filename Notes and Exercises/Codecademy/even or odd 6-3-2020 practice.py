#Even or Odd
#This program has the user input an integer and then says if it's even or odd

#use the input command to have the user input a number as the variable number
  #note: int() used here to convert to number rather than string
number = int(input('Please enter an integer: '))
#create a new variable that does the calculation
mod = number % 2
#basic if statements based on the modulo result
if mod == 0:
    print('Your number is Even')
elif mod != 0:
    print('Your number is Odd')
else:
    print('That is not an integer, asshole')
