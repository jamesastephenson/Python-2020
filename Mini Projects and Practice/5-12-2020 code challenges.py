#Write a function that takes a word and gives the numver of unique letters in-
#-that word
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
# Write your unique_english_letters function here:
def unique_english_letters(word):
  uniques = 0
  for letter in letters:
    if letter in word:
      uniques += 1
  return uniques
print(unique_english_letters("Apple"))

#Write a function that takes a word and x as arguments and counts the number-
#of times x appears in that word
def count_char_x(word, x):
  x_count = 0
  for i in word:
    if i == x:
      x_count += 1
  return x_count
print(count_char_x("mississippi", "s"))

#write a function that says the amount of a multi-char string x in word
def count_multi_char_x(word, x):
  #make a new list that is split around the string x
  x_split = word.split(x)
  #the return statement is len(x_split) - 1 because the list is now longer-
  #due to the split, we subtract because the list length is larger
  return len(x_split) - 1
print(count_multi_char_x("mississippi", "iss"))

#write a function that takes a string named word, a char start and a char end
#this function should return the substring between the first occurence of-
#-start and end in word. If start or end are not in word, function should return word
def substring_between_letters(word, start, end):
  #using the find command to find the start and end indeces in word
  start_char = word.find(start)
  end_char = word.find(end)
  if start_char and end_char == -1:
    return word
  elif start_char and end_char != -1:
    #start_char+1 is so we don't include the start character that we inputted
    #end_char is non inclusive
    return word[start_char+1:end_char]
print(substring_between_letters("apple", "p", "e"))

#write a function that takes a sentence string and an integer x
#return True if the string contains no words longer than x
#return False if any words are shorter than x
def x_length_words(sentence, x):
  split_sentence = sentence.split(' ')
  for word in split_sentence:
    if len(word) < x:
      return False
    else:
      return True

#write a function that takes two strings, sentence and name
#return True if name is in sentence REGARDLESS OF CAPITALIZATION
def check_for_name(sentence, name):
  #we still iterate through each item in the list sentence
  for word in sentence:
    #for this if statement we convert it all to lower
    #this makes cases not matter
    #in keeps the code tight for the search
    if name.lower() in sentence.lower():
      return True
    else:
      return False

#write a function that prints every other letter of input word
def every_other_letter(word):
  new_word = ''
  #set an empty variable and add the corresponding characters by iterating
  #setting the range for this is important for correct values
  for char in range(0, len(word), 2):
    new_word += word[char]
  return new_word

#write a function that returns an input word in reverse
def reverse_string(word):
  reverse = ""
  #set an empty variable then add to it by iterating through the range
  #note: in this range we are counting backwards
  #note2: this is why the third value in parentheses is -1
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse

#write a function that swaps the first letters of two input words
def make_spoonerism(word1, word2):
  new_word1 = word2[0] + word1[1:]
  new_word2 = word1[0] + word2[1:]
  return new_word1 + ' ' + new_word2

#adds exclamation points until string is 20 characters long
def add_exclamation(word):
  while(len(word) < 20):
    #note: I guess you can just += into strings
    word += "!"
  return word
