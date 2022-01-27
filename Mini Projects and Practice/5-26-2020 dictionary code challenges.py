#Sum Values
#write a function that takes a dictionary as a parameter and returns the-
#-sum of the values of the dictionary
def sum_values(my_dictionary):
  dict_sum = 0
  for value in my_dictionary.values():
    dict_sum += value
  return dict_sum
print(sum_values({"milk":5, "eggs":2, "flour": 3}))

#Even Keys
#create a function that takes a dictionary and returns the sum of the-
#-values of all even keys
def sum_even_keys(my_dictionary):
  total = 0
  for key in my_dictionary.keys():
    if key%2 == 0:
      total += my_dictionary[key]
  return total

#Add Ten
#Write a function that takes a dictionary and adds 10 to every value
def add_ten(my_dictionary):
  #loop through each key in the dictionary
  for key in my_dictionary:
    #my_dictionary[key] syntax indicates we're referring to that value in the pair
    # += to add 10 to each value in the dictionary
    my_dictionary[key] += 10
  return my_dictionary

#Values That Are Keys
#write a function that takes a dictionary and returns a list of-
#-all values in the dictionary that are also keys
def values_that_are_keys(my_dictionary):
  #define an empty list we can append to
  lst = []
  #loop iterates through the values in the dictionary
  for value in my_dictionary.values():
    #"if" "in" syntax here is seeing if the value is within a dictionary-
    #- (in this case, the dictionary's keys)
    if value in my_dictionary.keys():
      #add the corresponding values to the empty lst we defined
      lst.append(value)
  return lst

#Largest Value
#return the largest value in the dictionary and its key
def max_key(my_dictionary):
  #setting filler key and value with lowest possible value (float('-inf'))
  largest_key = float("-inf")
  largest_value = float("-inf")
  #looping through items in dictionary
  #'for key, value in' refers to us accessing the respective keys and values
  for key, value in my_dictionary.items():
    #if statement for when the value is larger than our established largest_value
    if value > largest_value:
      #set value and key to corresponding value and key in dictionary loop
      largest_value = value
      largest_key = key
  #DON'T FORGET TO RETURN
  return largest_key

#Word Length Dict
#take a list of strings named word as a parameter
#function should return a dictionary of key:value pairs
#value should be the length of each word
def word_length_dictionary(words):
  #setting an empty dict we can add to
  word_lengths = {}
  #looping through the words list
  for word in words:
    #add the length to our new dictionary as the value
    word_lengths[word] = len(word)
  return word_lengths

#Frequency Count
#function should take a list of elements named words
#function should return a dictionary containing the-
#-frequency of each element in words
def frequency_dictionary(words):
  #set empty dictionary
  new_dictionary = {}
  #loop through the word list
  for word in words:
    #if statement for if the word hasn't appeared yet
    if word not in new_dictionary:
      #set the value to 1 since that's its new frequency
      new_dictionary[word] = 1
    #elif statement for if word already appeared
    elif word in new_dictionary:
      #+=1 to the key to establish the new count
      new_dictionary[word] += 1
  return new_dictionary

#Unique Values
#function should take a dictionary and return the-
#-number of unique values in the dictionary
def unique_values(my_dictionary):
  #set empty list we can add to
  seen_values = []
  #loop through the values in the dictionary
  for value in my_dictionary.values():
    #if statement for when the value is not already in-
    #our seen_values list
    if value not in seen_values:
      #append the value to the list
      seen_values.append(value)
  #return the len because we want the number of unique values,-
  #-not the values themselves
  return len(seen_values)

#Count First Letter
#function should take a dictionary named names
#function should return a new dictionary where each key-
#-is the first letter of a last name, and the value is the-
#-number of people whose last name begins with that letter
def count_first_letter(names):
  #define empty dictionary called letters
  letters = {}
  #looping through the key in the names dictionary
  for key in names:
    #establish that first_letter will refer to the 0 index-
    #-of each key 'key[0]'
    first_letter = key[0]
    if first_letter not in letters:
      letters[first_letter] = 0
    letters[first_letter] += len(names[key])
  return letters
