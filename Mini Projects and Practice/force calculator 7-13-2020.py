#Force Calculator
#asks the user to input which value they want to calculate, then asks for the values and prints the final result
#does not require units to be mentioned, contains an error message if an invalid choice is picked
#F = M * A

choice = input('Would you like to find \'Force,\' \'Mass,\' or \'Acceleration,\'? \n>')

if choice.lower() == 'force':
    mass = input('Please enter the object\'s mass \n>')
    acceleration = input('Please enter the object\'s acceleration \n>')
    force = float(mass) * float(acceleration)
    print('Force: ' + str(force) + ' Newtons')

elif choice.lower() == 'mass':
    force = input('Please enter the Force of your object: \n>')
    acceleration = input('Please enter the object\'s acceleration \n>')
    mass = float(force) / float(acceleration)
    print('Mass: ' + str(mass) + ' Kg')

elif choice.lower() == 'acceleration':
    force = input('Please enter the Force of your object: \n>')
    mass = input('Please enter the object\'s mass \n>')
    acceleration = float(force) / float(mass)
    print('Acceleration: ' + str(acceleration) + 'm/s')

else:
    choice = input('Invalid input.')
