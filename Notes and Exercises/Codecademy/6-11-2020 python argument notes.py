#Parameters and Arguments
#some definitions:
  #a parameter is a variable in the definition of a function
  #an argument is the value being passed into a function call
  #a function definition begins with def and contains the following indented block
  #function calls are the places a function is invoked

#None: It's Nothing
  #how do you define a variable that you can't assign a value to yet?
    #you use None
  #None is a special value in Python
    #it is unique (there can't be two different Nones)
    #it is immutable (you can't update None or assign new attributes to it)
none_var = None
if none_var:
    print("Hello!)
else:
    print("Goodbye")
#prints Goodbye because None evaluates to false
  #None is falsy, meaning that it evaluates to False in an if statement
  #None is also unique, which means that you can test if something is None-
  #-using the is keyword
# first we define session_id as None
session_id = None
if session_id is None:
  print("session ID is None!")
  # this prints out "session ID is None!"
# we can assign something to session_id
if active_session:
  session_id = active_session.id
# but if there's no active_session, we don't send sensitive data
if session_id is not None:
  send_sensitive_data(session_id)
  #above we initialize our session_id to None, then set our session_id-
  #-if there is an active session
  #since session_id could either be None we check if session_id is None-
  #-before sending out sensitive data
from review_lib import get_next_review, submit_review
review = get_next_review()
if review is not None:
  submit_review(review)

#Default Return
  #a function without a return statement will return None after competing
    #this means all functions in python return something whether it's explicit or not
def no_return():
  print("You've hit the point of no return")
  # notice no return statement
here_it_is = no_return()
print(here_it_is)
# Prints out "None"
  #a return statement without any value returns None also
  #with testing for None we can see where an error may have occured

# store the result of this print() statement in the variable prints_return
prints_return = print("What does this print function return?")
#prints the string
# print out the value of prints_return
print(prints_return)
#prints None
# call sort_this_list.sort() and save that in list_sort_return
sort_this_list = [14, 631, 4, 51358, 50000000]
list_sort_return = sort_this_list.sort()
# print out the value of list_sort_return
print(list_sort_return)
#prints None

#Default Arguments
  #function arguments are required in function, so a standard function definition-
  #-that defines two parameters requires two arguments passed into the function
  #not all function arguments in python need to be rquired
    #if we give a default argument to a python function, that argument-
    #-won't be required when we call the function

# Function defined with one required and one optional parameter
def create_user(username, is_admin=False):
  create_email(username)
  set_permissions(is_admin)
# Calling with two arguments uses the default value for is_admin
user2 = create_user('djohansen')
  #above we set the is_admin parameter to have the default argument False

# We can make all three parameters optional
def create_user(username=None, is_admin=False):
  if username is None:
    username = "Guest"
  else:
    create_email(username)
  set_permissions(is_admin)
# So we can call with just one value
user3 = create_user('ssylvain')
# Or no value at all, which would create a Guest user
user4 = create_user()
  #above we define the function with all optional parameters
  #if we call with one argument that gets interpreted as username
  #if we call without any arguments, it would use the default values

#Using Keyword and Positional Arguments
  #python will only accept functions defined with their parameters in a specific order
  #the required parameters need to occur before any parameters with a default argument
# Raises a TypeError
def create_user(is_admin=False, username, password):
  create_email(username, password)
  set_permissions(is_admin)
  #in the above code, we attempt to give a default for is_admin without-
  #-defining default arguments for the later parameters
  #if we want to give is_admin a default argument, we need to put it last
# Works perfectly
def create_user(username, password, is_admin=False):
  create_email(username, password)
  set_permissions(is_admin)

#Keyword Arguments
  #when we call a function in python, we need to list the arguments to that function-
  #-to match the order of the parameters in the function definition
    #we don't necessarily need to do this if we pass keyword arguments
  #we use keyword arguments by passing arguments to a function with a-
  #-special syntax that uses the names of the parameters
    #this is useful if the function has many optional default arguments-
    #-or if the order of a function's parameters is hard to tell
# Define a function with a bunch of default arguments
def log_message(logging_style="shout", message="", font="Times", date=None):
  if logging_style == 'shout':
    # capitalize the message
    message = message.upper()
  print(message, date)
# Now call the function with keyword arguments
log_message(message="Hello from the past", date="November 20, 1693")
  #above we defined log_message() which can take 0 to 4 arguments
  #since it's not clear which order the four arguments might be defined in,-
  #-we can use the parameter names to call the function
    #notice the syntax message="Hello from the past"
    #the key word message here needs to be the name of the parameter we-
    #-are trying to pass the argument to

#Don't Use Mutable Default Arguments
  #while it may be tempting to define an empty list as a default argument,-
  #-it will not populate the way you want it to
    #all subsequent function calls will modify the same list
  #a mutable object refers to a data structure that is intended to be changed
  #int, float, and other numbers can't be mutated
  #tuples are a kind of immutable list
  #strings are also immutable

#Using None as a Sentinel
  #what can we use instead of a list as a default argument for a function?
  #we can use None as a special value to indicate we didn't receive anything
  #after we check whether an argument was provided, we can instantiate a-
  #-new list if it wasn't
def add_author(authors_books, current_books=None):
  if current_books is None:
    current_books = []

  current_books.extend(authors_books)
  return current_books
  #in the above function we accept current_books a value expected to be a list
  #but we don't require it
  #if someone calls add_author() without giving an argument for current_books-
  #-we supply an empty list
  #this way multiple calls to add_author won't include data from previous calls
def update_order(new_item, current_order=None):
  if current_order is None:
    current_order = []
  current_order.append(new_item)
  return current_order

#Unpacking Multiple returns
  #a function can return multiple things
  #in Python we can return multiple pieces of data by separating each variable-
  #-with a comma
def multiple_returns(cool_num1, cool_num2):
  sum_nums = cool_num1 + cool_num2
  div_nums = cool_num1 / cool_num2
  return sum_nums, div_nums
  #above we created a function that returns two results
#what happens when we call this function?
sum_and_div = multiple_returns(20, 10)
print(sum_and_div)
# Prints "(30, 2)"
print(sum_and_div[0])
# Prints "30"
  #we get those values back as a tuple
    #tuples are immutable list-like objects indicated by parentheses
  #we can index into the tuple in the same way as a list
    #ie. sum_and_div[0]
  #what if we want to save these two results in separate variables?
    #we can by unpacking the function return
    #we can list our new variables comma-separated that correspond to the-
    #-number of values returned
sum, div = sum_and_div(18, 9)
print(sum)
# Prints "27"
print(div)
# Prints "2"

def scream_and_whisper(text):
    scream = text.upper()
    whisper = text.lower()
    return scream, whisper
the_scream, the_whisper = scream_and_whisper('Yelling')

#Positional Argument Unpacking
  #we don't always know how many arguments a function is going to receive-
  #-and sometimes we want to handle any possibility that comes at us
  #Python gives us two methods for unpacking arguments provided to functions
    #first is called Positional Argument Unpacking:
def shout_strings(*args):
  for argument in args:
    print(argument.upper())
shout_strings("hi", "what do we have here", "cool, thanks!")
# Prints out:
# "HI"
# "WHAT DO WE HAVE HERE"
# "COOL, THANKS!"
  #in shout_strings() we use a single asterisk (*) to indicate we'll accept-
  #-any number of positional arguments passed to the function
  #our parameter args is a tuple of all the arguments passed
    #in this case args has three values inside, but it can have many more
  #notice that args is just a parameter name and we aren't limited to that name
    #although using args is a fairly standard practice
  #we can also have other positional parameters before our *args parameter
def truncate_sentences(length, *sentences):
  for sentence in sentences:
    print(sentence[:length])
truncate_sentences(8, "What's going on here", "Looks like we've been cut off")
# Prints out:
# "What's g"
# "Looks li"
  #above we defined a function truncate_sentences that takes a length parameter-
  #-and also any number of sentances
  #the function prints out the first length many characters of each sentence-
  #-in sentences
from os.path import join

path_segment_1 = "/Home/User"
path_segment_2 = "Codecademy/videos"
path_segment_3 = "cat_videos/surprised_cat.mp4"

# join all three of the paths here!
print(join(path_segment_1, path_segment_2, path_segment_3))

def myjoin(*args):
  joined_string = args[0]
  for arg in args[1:]:
    joined_string += arg
  return joined_string

#Keyword Argument Unpacking
  #python also allows us to define functions with unlimited keyword parameters
  #the syntax is similar to PAU but uses two asterisks (**) instead of one
  #instead of args, we call this kwargs as a shorthand for keyword arguments
def arbitrary_keyword_args(**kwargs):
  print(type(kwargs))
  print(kwargs)
  # See if there's an "anything_goes" keyword arg
  # and print it
  print(kwargs.get('anything_goes'))

arbitrary_keyword_args(this_arg="wowzers", anything_goes=101)
# Prints "<class 'dict'>
# Prints "{'this_arg': 'wowzers', 'anything_goes': 101}"
# Prints "101"
  #as you can see, **kewargs gives us a dictionary with all the keyword-
  #-arguments that were passed to arbitrary_keyword_args
    #we can access these arguments using standard dictionary methods
  #since we're not sure whether a keyword argument will exist, it's probably-
  #-best to use the dictionary's .get() method to safely retrieve the-
  #-keyword argument
    #if the key is not in the dictionary, .get() will return None

# Checkpoint 1
print("My name is {name} and I'm feeling {feeling}.".format(name="James", feeling="wired"))

# Checkpoint 2
from products import create_product

# Update create_products() to take arbitrary keyword arguments
def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

# Checkpoint 3
# Update the call to `create_products()` to pass in this dictionary as a series of keyword
create_products(
  baseball= 3,
  shirt = 14,
  guitar= 70
)


#Using Both Keyword and Positional Unpacking
  #This keyword argument unpacking syntax can be used even if the function-
  #-takes other parameters
  #However, the parameters must be listed in this order
    #all named positional parameters
    #an unpacked positional paremeter (*args)
    #all named keyowrd parameters
    #an unpacked keyword paremeter (**kwargs)
#here's a function with all possible types of parameter:
def main(filename, *args, user_list=None, **kwargs):
  if user_list is None:
    user_list = []

  if '-a' in args:
    user_list = all_users()

  if kwargs.get('active'):
    user_list = [user for user_list if user.active]

  with open(filename) as user_file:
    user_file.write(user_list)
  #looking at the signature of main() we define four different kinds of parameters
    #first, the filename is a normal required positional parameter
    #second, *args, is all positional arguments given to a function after that-
    #-organized as a tuple in the parameter args
    #third, user_list is a keyword parameter with a default value
    #last, **kwargs is all other keyword arguments assembled as a dictionary in the parameter kwargs
#a possible call to the function could look like this
main("files/users/userslist.txt", 
     "-d", 
     "-a", 
     save_all_records=True, 
     user_list=current_users)
#in the body of main() these arguments would look like this
    #filename == "files/users/userslist.txt"
    #args ==('-d', '-a)
    #user_list == current_users
    #kwargs == {'save_all_records': True}
  #we can use these four kinds of parameters to create functions that handle-
  #-a lot of possible argumetns being passed to them

def remove(filename, *args, **kwargs):
  with open(filename) as file_obj:
    text = file_obj.read()
  for arg in args:
    text = text.replace(arg, "")
  for kwarg, replacement in kwargs.items():
    text = text.replace(kwarg, replacement)
  return text

print(remove("text.txt", "generous", "gallant", fond="amused by", Robin="Mr. Robin"))

#Passing Containers As Arguments
  #python also supports a syntax that makes deconstructing any data that you-
  #-have on hand feed into a function that accepts these kinds of unpacked arguments
  #the syntax is very similar, but is used when a function is called
def takes_many_args(*args):
  print(','.join(args))

long_list_of_args = [145, "Mexico City", 10.9, "85C"]

# We can use the asterisk "*" to deconstruct the container.
# This makes it so that instead of a list, a series of four different
# positional arguments are passed to the function
takes_many_args(*long_list_of_args)
# Prints "145,Mexico City,10.9,85C"

  #we can use * when calling the function that takes a series of positional-
  #-parameters to unwrap a list or a tuple
  #this makes it easy to provide a sequence of arguments to a function-
  #-even if that function doesn't take a list as an argument
#similarly we can use ** to destructure a dictionary
def pour_from_sink(temperature="Warm", flow="Medium")
  set_temperature(temperature)
  set_flow(flow)
  open_sink()

# Our function takes two keyword arguments
# If we make a dictionary with their parameter names...
sink_open_kwargs = {
  'temperature': 'Hot',
  'flow': "Slight",
}

# We can destructure them an pass to the function
pour_from_sink(**sink_open_kwargs)
# Equivalent to the following:
# pour_from_sink(temperature="Hot", flow="Slight")

  #so we can also use dictionaries and pass them into functions as keyword-
  #-arguments with that syntax
  #notice that our pour_from_sink() function doesn't even accept arbitrary **kwargs
  #we can use this destructuring syntax even when a function has a specific-
  #-number of keyword or positional arguments it accepts
  #we just need to be careful that the object we're destructuring matches the-
  #-length (and names, if a dictionary) of the signature of the function we're-
  #-passing it into

from products import create_product

def create_products(**products_dict):
  for name, price in products_dict.items():
    create_product(name, price)

new_product_dict = {
  'Apple': 1,
  'Ice Cream': 3,
  'Chocolate': 5,
}

# Call create_product() by passing new_product_dict
# as kwargs!
create_products(**new_product_dict)


