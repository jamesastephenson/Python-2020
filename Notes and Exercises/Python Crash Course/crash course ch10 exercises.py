#10-1
#note: had to re-open the file for each of these, hence the with open() lines

with open("learning_python.txt","r") as f:
    #print the entire file
    contents = f.read()
    print(contents)

with open("learning_python.txt","r") as f:
    #looping over the file object
    for line in f:
        print(line)

with open("learning_python.txt","r") as f:
    #saving the function as a list with readlines, then printing
    lines = f.readlines()
    for line in lines:
        print(line)

#10-2
with open("learning_python.txt","r") as f:
    contents2 = f.read().replace("Python", "Java")
    #note: first argument is the string to replace, second is what it gets replaced with
    #contents2.replace("Python", "Java")  this block is commented out, needed to be in var assignment
    print(contents2)

#10-3
filename_10_3 = "guest.txt"
#opening file in write mode since we're writing to it
with open(filename_10_3, "w") as f:
    user_name = input("Hello, what is your name? \n>")
    f.write(user_name)

#10-4
filename_10_4 = "guest_book.txt"
question_10_4_loop = True

#while loop will continue unless user enters "q" to break the loop
while question_10_4_loop == True:
    name = input("Hello! Please enter your name. (enter 'q' to quit) \n>")
    if name == "q":
        break
    #opening file in append mode since we're adding to it
    with open(filename_10_4, "a") as f:
        f.write(name)
        #newline f.write() is here for formatting
        #otherwise it just puts the next name immediately after the prev one
        f.write("\n")

#10-5
filename_10_5 = "WhyWeLoveProgramming.txt"
question_10_5_loop = True

while question_10_5_loop == True:
    user_entry = input("What do you love about programming? (enter 'q' to quit) \n>")
    if user_entry == "q":
        break
    with open(filename_10_5, "a") as f:
        f.write(user_entry)
        f.write("\n")

#10-6 / 10-7
question_10_6_loop = True

while question_10_6_loop == True:
    try:
        num1 = input("Please enter the first number to add (enter 'q' for both numbers to quit): \n>")
        num2 = input("Please enter the second number to add (enter 'q' for both numbers to quit): \n>")
        if num1 == "q":
            break
        if num2 == "q":
            break
        int1 = int(num1)
        int2 = int(num2)
    except ValueError:
        print("Please enter a numerical value.")
    else:
        add_result = int1 + int2
        print(f"{num1} plus {num2} equals {add_result}")
#note: made this one a little more convoluted than necessary, order it better in the future

#10-8
#to fulfil what the question wants, just make a try-except block that handles a FileNotFound error
try:
    with open("cats.txt", "r") as f:
        cat_total = f.read()
        print(cat_total)
except FileNotFoundError:
    print("Your file is not available")
#will print the statement in the except block because the file doesn't exist
#for 10-9, could comment out the print statement or have a different message

#10-10
with open("art_of_war.txt", "r") as f:
    full_text = f.read()
    split_lower_text = full_text.lower().split()
    war_count = split_lower_text.count("war")
    print(f"Your text file contains {war_count} mentions of the word 'war.'")
