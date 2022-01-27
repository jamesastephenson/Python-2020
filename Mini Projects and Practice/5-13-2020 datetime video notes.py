#datetime is basically a python object that represents a point in time
#datetime is a very useful module because that info is v versatile

from datetime import datetime

#create a date using year, month, and day as arguments
birthday = datetime(1994, 8, 20, 2, 14, 2) #going (month, day, year, hour in military, minute, second)
print(birthday.year) #1994
print(birthday.hour) #2

#datetime.now() will get us our exact moment when the program is run
#will continually update when Python executes code
datetime.now()

#we can subtract datetimes to get a time difference
year_diff = datetime(2018, 1, 1) - datetime(2017, 1, 1)
print(year_diff)
#we can only really subtract, not multiply or add etc


#strptime function lets us parse a datetime out of a string
#dates are often stored in strings
#python can convert a string into a datetime with strptime function
parse_date = datetime.strptime('Jan 15, 2018', '%b %d, %Y')
#first argument is the string in question, second argument is a formatted string
#tells python how the string is formatted
#these are the % codes in the above example, check online for list as needed
#we've told python the format of our date string now

print(parse_date.month) #prints 1 which is correct b/c january
print(parse_date.year) #prints 2018, the year we formatted in


#strftime let's us take a datetime and put specific parts of it into a sgtring
date_string = datetime.strftime(datetime.now(),'%b %d, %Y')
#first argument is a datetime
#second argument is a formatted string, but we're creating a string from-
#-a datetime instead, essentially the opposite of strptime example
print(date_string)
