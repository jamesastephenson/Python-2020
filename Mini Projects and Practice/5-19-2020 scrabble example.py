letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

#converts all letters to lower case, prevents confusing upper and lower
#setting letters list equal to an iteration that converts to lower case
letters += [letter.lower() for letter in letters]

#creates a dictionary that zips the letters and points together
#syntax: {keys:values for keys, values in zip(keys, values)}
letter_to_points = {letters:points for letters, points in zip(letters, points)}
#adding the blank space to the letter_to_points dictionary for 0 points
letter_to_points[' '] = 0
#test print
print(letter_to_points)

#defining function that adds up the score for each word by iterating through the letters
def score_word(word):
  #defining blank value for point total
  point_total = 0
  #iterating through each letter in the word with thi loop
  for letter in word:
    #+= to the point total
    #letter_to_points is the dictionary, .get() lets us find the corresponding point value
    #.get(letter, 0). the 0 is a default value if the character is not in our dictionary
    point_total += letter_to_points.get(letter, 0)
  #return point_total after function is carried out
  return point_total

#testing our function with the example word BROWNIE. we set it to a variable and print
brownie_points = score_word('BROWNIE')
print(brownie_points)

#new dictionary of players (key) and value lists (their entered words)
player_to_words = {'player1': ['BLUE', 'TENNIS', 'EXIT'], 'wordNerd': ['EARTH', 'EYES', 'MACHINE'], 'Lexi Con': ['ERASER', 'BELLY', 'HUSKY'], 'Prof Reader': ['ZAP', 'COMA', 'PERIOD']}
#defining an empty dictionary to account for point totals
player_to_points = {}

#iterating through the player_to_words dictionary
for player, words in player_to_words.items():
  #setting empty value to add to
  player_points = 0
  #iterating through each word individually to calculate total points
  for word in words:
    #using our above function on the word and setting equal to player_points
    player_points += score_word(word)
  #setting the player_points value from inside the loop to player
  #player_to_points[player] syntax because we're affecting a dictionary
  #it is indented like this so it is assigned to each player as it iterates
  player_to_points[player] = player_points
print(player_to_points)

#extra
#function takes a player and a word as an argument
#adds word to player's section in dictionary
def play_word(player, word):
  player_to_words[player].append(word)
