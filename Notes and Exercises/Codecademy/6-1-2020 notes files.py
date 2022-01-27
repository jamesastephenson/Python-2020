#LEARN PYTHON: FILES
#note: these use codecademy examples, so the files aren't on our pc
#pay attention to the syntax
#Reading a file
    #computers use file systems to store and retrieve data
with open('real_cool_document.txt') as cool_doc:
  cool_contents = cool_doc.read()
print(cool_contents)
    #this code block opens a file objecdt called cool_doc
    #it also creates a new indented block where you can read the contents
    #we then read the contents of the file cool_doc using cool_doc.read()
    #we save the resulting string into the variable cool_contents
    #then we print cool_contents which outputs our statement
with open('welcome.txt') as text_file:
  text_data = text_file.read()
print(text_data)

#Iterating Through Lines
    #if we want to store each line of a file in a variable, we use .readlines()
    #.readlines() is a function that reads a text file line by line instead of all at once
with open('how_many_lines.txt') as lines_doc:
  for line in lines_doc.readlines():
    print(line)
    #in this example we use a for loop to iterate through each line in the doc

#Reading a Line
    #.readline() will only read a single line at a time
    #we use this when we don't want to iterate through a whole file
    #if the entire doc is read line by line in this way, subsequent-
    #calls to .readline() will start returning an empty string ('')
with open('millay_sonnet.txt') as sonnet_doc:
  first_line = sonnet_doc.readline()
  second_line = sonnet_doc.readline()
  print(second_line)
    #this script also creates a file object called sonnet_doc that points to-
    #-the file millay_sonnet.txt
    #it then reads in the first line using sonnet_doc.readline() and saves-
    #-that to the variable first_line
    #it then saves the second line into the variable second_line and prints it out
with open('just_the_first.txt') as first_line_doc:
  first_line = first_line_doc.readline()
  print(first_line)

#Writing a File
    #what if we want to create a file of our own?
    #the open() function needs another argument to open a file to write to
with open('generated_file.txt', 'w') as gen_file:
  gen_file.write("What an incredible file!")
    #Here we pass the argument 'w' to open() in order to indicate to-
    #-open the file in write-mode
    #The default argument is 'r' and passing 'r' to open() opens the file-
    #-in read mode as we've been doing
    #This code creates a new file in the same folder as script.py and-
    #-gives it the text 'What an incredible file!'
    #note: if there is already a file with the same name, it will overwrite
with open('bad_bands.txt', 'w') as bad_bands_doc:
  bad_bands_doc.write('Bush')

#Appending to a File
    #to add to a file without overwriting, we open the file using the 'a'-
    #-argument for append-mode. this is instead of 'w' for write-mode
with open('generated_file.txt', 'a') as gen_file:
  gen_file.write("... and it still is")
    #This code opens a file object in the temporary variable gen_file
    #The variable points to the file generated_file.txt and adds the line-
    #-'... and it still is' as a new line in the file.
    #This is because we are in append-mode
  #Notice that opening the file in append-mode means that using the file object's-
  #.write() method appends whatever is passed to the end of the file in a new line
with open('cool_dogs.txt', 'a') as cool_dogs_file:
  cool_dogs_file.write('Air Buddy')

#What's With 'with'
  #We've been opening files with the 'with' keyword so far
  #The with keyword is a context manager for the file we're calling open() on
  #This context manager takes care of opening the file when we call open()-
  #-and then closing the file after we leave the indented block
#Why is closing the file so complicated
  #Most other aspects of our code deal with things that Python itself controls
  #All variables you create are Python objects
      #Python knows how to clean them up when it's done with them
  #Since files exist outside of your Python script, we need to tell Python-
  #-that we're done with them so it can close the connection to that file
  #Leaving a file connection open unnecessarily can affect performance
#The with syntax replaces older ways to access files where you need to call.close()-
#- on the file object manually
  #we can still open up a file and append to it with the old syntax
  #however, if we use the older syntax, we must remember to close the file afterwards
      #because this is more verbose, using with is preferred
with open('fun_file.txt') as close_this_file:
setup = close_this_file.readline()
punchline = close_this_file.readline()
print(setup)

#What Is a CSV File?
  #CSV files are an example of a text file that structures its data
  #CSV stands for Comma-Separated Values
    #They are usually the way data from spreadsheets is exported to a portable format
  #in a CSV file, spreadsheet data is represented by commas between each-
  #-item, corresponding to the rows in the spreadsheet
  #CSVs are text files, so they can be opened the same way
with open('logger.csv') as log_csv_file:
  print(log_csv_file.read())

#Reading a CSV File
  #There are ways to access CSV data in a format better suited for programming
  #in Python we can convert that data into a dictionary
    #to do this we use the csv library's DictReader object
import csv
list_of_email_addresses = []
with open('users.csv', newline='') as users_csv:
  user_reader = csv.DictReader(users_csv)
  for row in user_reader:
    list_of_email_addresses.append(row['Email'])
  #In the above code:
    #we import our csv library which gives us tools to parse the CSV file
    #we create the empty list that we'll later populate with email addresses
    #then we open the users.csv file with the temp variable users_csv
      #the keyword argument newline='' is used so we don't accidnetally-
      #-mistake a line break in our data fields as a new row in our CSV
    #after opening, we use csv.DictReader(users_csv) which converts the lines-
    #-of our CSV file to Python dictionaries which we can use access methods for
      #The keys of our dictionary are, by default, the entries in the first-
      #-line of our CSV file
      #Since our CSV's first line calls the third field in our CSV 'Email',-
      #-we can use that as the key in each row of our DictReader
    #When we iterate through the rows of our user_reader object, we access-
    #-all of the rows in our CSV as dictionaries (except the first row which-
    #-we used to label the keys of our dictionary)
    #By accessing the 'Email' key of each of these rows, we can grab the-
    #-email address in that row and append it to our list
import csv
with open('cool_csv.csv') as cool_csv_file:
  cool_csv_dict = csv.DictReader(cool_csv_file)
  for row in cool_csv_dict:
    print(row['Cool Fact'])

#Reading Different Types of CSV Files
  #CSV files can be separated by characters other than commas
    #TSV files - Tab Separated Files
  #We call all files with a list of different values a CSV file and then-
  #-use different delimiters (like , or tab) to indicate where the values-
  #-start and stop
    #for example, a list of addresses would include commas-
    #-therefore we would use semicolons in their place to differentiate entries
  #the \n charcter is the escape sequence for a new line
    #the possibility of a new line escaped by a \n character is why we pass-
    #- the newline='' keyword argument to the open() function
import csv
with open('addresses.csv', newline='') as addresses_csv:
  address_reader = csv.DictReader(addresses_csv, delimiter=';')
  for row in address_reader:
    print(row['Address'])
  #notice when we call csv.DictReader we pass in the delimiter parameter
    #(the string that's used to deliniate separate fields in the CSV)
  #we then iterate through the CSV and print out each of the addresses
import csv
with open('books.csv') as books_csv:
  isbn_list = []
  books_reader = csv.DictReader(books_csv,delimiter='@')
  for book in books_reader:
    isbn_list.append(book['ISBN'])

#Writing a CSV File
big_list = [{'name': 'Fredrick Stein', 'userid': 6712359021, 'is_admin': False}, {'name': 'Wiltmore Denis', 'userid': 2525942, 'is_admin': False}, {'name': 'Greely Plonk', 'userid': 15890235, 'is_admin': False}, {'name': 'Dendris Stulo', 'userid': 572189563, 'is_admin': True}] 
import csv
with open('output.csv', 'w') as output_csv:
  fields = ['name', 'userid', 'is_admin']
  output_writer = csv.DictWriter(output_csv, fieldnames=fields)
  
  output_writer.writeheader()
  for item in big_list:
    output_writer.writerow(item)
  #in our code above, we had a set of dictionaries with the same keys for each
  #we import the csv library and then open a new CSV file in write mode
    #(passing the 'w' argument to the open() function
  #we define the fields that we're going to be using into a variable called fields
  #we instantiate our CSV writer and pass two arguments
    #first is output_csv, the file handler object
    #second is our list of fields fields, which we pass to the keyword parameter-
    #-fieldnames
  #now that we've instantiated our CSV file writer, we can add lines to the file itself
  #first we want the headers, so we call .writerheader() on the writer object
    #this writes all the fields passed to fieldnames as the first row in our file
  #each item in big_list is a dictionary with each field in fields as the keys
  #we call output_writer.writerow with the item dictionaries which writes-
  #-each line to the CSV file
access_log = [{'time': '08:39:37', 'limit': 844404, 'address': '1.227.124.181'}, {'time': '13:13:35', 'limit': 543871, 'address': '198.51.139.193'}, {'time': '19:40:45', 'limit': 3021, 'address': '172.1.254.208'}, {'time': '18:57:16', 'limit': 67031769, 'address': '172.58.247.219'}, {'time': '21:17:13', 'limit': 9083, 'address': '124.144.20.113'}, {'time': '23:34:17', 'limit': 65913, 'address': '203.236.149.220'}, {'time': '13:58:05', 'limit': 1541474, 'address': '192.52.206.76'}, {'time': '10:52:00', 'limit': 11465607, 'address': '104.47.149.93'}, {'time': '14:56:12', 'limit': 109, 'address': '192.31.185.7'}, {'time': '18:56:35', 'limit': 6207, 'address': '2.228.164.197'}]
fields = ['time', 'address', 'limit']

import csv
#import csv
with open('logger.csv', 'w') as logger_csv:
#opening logger.csv file with 'w' as argument to initiate writing-mode
#logger_csv is our variable to work with in python
  log_writer = csv.DictWriter(logger_csv, fieldnames=fields)
  
  log_writer.writeheader()
  for item in access_log:
  #loop through the initial list
    log_writer.writerow(item)
    #using the writerow command to add item to our log_writer object

#Reading a JSON File
  #SCV isn't the only file format that Python has a built in library for
  #JSON is an abbreviation of JavaScript Object Notation
    #a file format inspired by JavaScript
    #name is a bit of a misnomer because some JSON is not valid JavaScript
  #JSON's format is similar to Python dictionary syntax
    #may make it easy to read from a Python dev standpoint
  #Python comes with a json package that will help us parse JSON files-
  #-into actual python dictionaries
import json
#first we import the json package
with open('purchase_14781239.json') as purchase_json:
#open the file with the open() command
  #we're opening in read mode, so we only need to pass the file name
  #we save the file in the temp variable purchase_json
  purchase_data = json.load(purchase_json)
  #we parse puchase_json using json.load()
    #this creates a Python dictionary out of the file
  #saving the results into purchase_data means we can interact with it
print(purchase_data['user'])
#we print out one of the values of the JSON file by keying into the purchase_data object

import json
with open('message.json') as message_json:
  message = json.load(message_json)
print(message['text'])

#Writing a JSON File
  #we can use the json library to translate Python objects to JSON as well
    #this is useful in instances where you're using a Python library to-
    #-serve seb pages, you would also be able to serve JSON
turn_to_json = {
  'eventId': 674189,
  'dateTime': '2015-02-12T09:23:17.511Z',
  'chocolate': 'Semi-sweet Dark',
  'isTomatoAFruit': True
}
#we want to turn this dictionary into a JSON file
import json
#first we import the json module
with open('output.json', 'w') as json_file:
#open a write-mode file under the variable json_file
  json.dump(turn_to_json, json_file)
  #use json.dump() method to write to the file
  #json.dump() takes to arguments:
    #first is the data object
    #second is the file object you want to save

data_payload = [
  {'interesting message': 'What is JSON? A web application\'s little pile of secrets.',
   'follow up': 'But enough talk!'}
]
import json
with open('data.json', 'w') as data_json:
  json.dump(data_payload, data_json)

#REVIEW:
#you are now able to
  #open file objects using open() and with
  #read a file's full contents using Python's .read() method
  #read a file line-by-line using .readline() and .readlines()
  #create new files by opening them in write mode
  #append to a file non-destructively by opening a file in append-mode
  #apply all of the above to different types of data carrying files
    #including CSV and JSON
