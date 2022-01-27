#HACKING THE FENDER
#goal is to update the passwords.txt file to scramble the data
#then add signature of Slash Null
#working with CSV and other text files

#import csv module to work with it
import csv
#create an empty list called compromised_users we can add to
compromised_users = []

#opening passwords.csv in read mode
with open('passwords.csv') as password_file:
  #set variable password_csv to the DictReader function
  password_csv = csv.DictReader(password_file)
  #now we iterate through each line of the CSV with a for loop
  for password_row in password_csv:
    #print(password_row['Username'] was used as a test to view the dict
    #use the append() method to add username to compromised_users
    #because it's a for loop, it will do this for each username
    compromised_users.append(password_row['Username'])
#exit out of this with block, we are done with passwords.csv

#open compromised_users.txt in write mode
with open('compromised_users.txt', 'w') as compromised_user_file:
  #for loop iterates over each user in compromised_users
  for user in compromised_users:
    #write the username of each user into compromised_user_file
      #note: str() had to be used because it wasn't accepting at first
    compromised_user_file.write(str(compromised_users))
#exit out of this with block

#import the json module
import json
#open a new json file in write-mode called boss_message.json
with open('boss_message.json', 'w') as boss_message:
  #create a dictionary object that relays a boss message
  #'recipient' key with value 'The Boss'
  #'message' key with value 'Mission Success'
  boss_message_dict = {
  'recipient': 'The Boss',
  'message': 'Mission Success'
  }
  #write boss_message_dict to boss_message using json.dump()
  #first argument is a Python data object (like a dictionary or array)
  #second argument is a file object to write the resulting json to
  json.dump(boss_message_dict, boss_message)

#create a new with block and open 'new_passwords.csv' in write-mode
with open('new_passwords.csv', 'w') as new_passwords_obj:
  #save the signature string to a variable
  #note: the triple quotes are used for multi line strings
  slash_null_sig = '''
   _  _     ___   __  ____             
/ )( \   / __) /  \(_  _)            
) \/ (  ( (_ \(  O ) )(              
\____/   \___/ \__/ (__)             
 _  _   __    ___  __ _  ____  ____  
/ )( \ / _\  / __)(  / )(  __)(    \ 
) __ (/    \( (__  )  (  ) _)  ) D ( 
\_)(_/\_/\_/ \___)(__\_)(____)(____/ 
        ____  __     __   ____  _  _ 
 ___   / ___)(  )   / _\ / ___)/ )( \
(___)  \___ \/ (_/\/    \\___ \) __ (
       (____/\____/\_/\_/(____/\_)(_/
 __ _  _  _  __    __                
(  ( \/ )( \(  )  (  )               
/    /) \/ (/ (_/\/ (_/\             
\_)__)\____/\____/\____/
'''
  #write slash_null_Sig to new_passwords_obj
  #now we have the file to replace passwords.csv with
  new_passwords_obj.write(slash_null_sig)
#Complete
