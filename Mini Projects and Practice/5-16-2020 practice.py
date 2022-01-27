def unique_english_letters(word):
    letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    uniques = 0
    for letter in letters:
        if letter in word:
            uniques += 1
    return uniques

def count_char_x(word, x):
    x_count = 0
    for char in word:
        if x == char:
            x_count += 1
    return x_count

def count_multi_char_x(word, x):
    #splitting word at string x and setting that to a value
    x_split = word.split(x)
    return len(x_split) - 1

