#chapter 10 notes

#pi_digits.txt is used as an example, it is stored in the same folder as these notes

#to open the text file
with open("pi_digits.txt") as file_object:
    contents = file_object.read()
print(contents)

#to work with a file, you need to open it to access it
#the open() function needs one argument: the file you want to open
    #python looks for the file in the directory where our program is automatically
#the open() function returns an object representing the file
    #python assigns this object to file_object which we'll work with later
#the keyword "with" closes the file once access to it is no longer needed
    #be careful not to call a close() method too early in your program

#our above code represents the number as 3 lines
    #this is because read() returns an empty string when it reaches the end of the file
    #we can use rstrip() to remove the extra blank line
print(contents.rstrip())

#if your file is not in the same directory as your program, you need to give the file path
#ie. with open("text_files/filename.txt") as file_object:


#if your file path is long, it may be worth setting to a variable in python for convenience
#ie. file_path = (big command needed to properly path file)


#you can use a for loop to examine a file one line at a time
filename = "pi_digits.txt"
with open(filename) as file_object:
    for line in file_object:
        #we use rstrip() in this print because an invisible newline char changed our formatting
        print(line.rstrip())

#making a list of lines from a file
#when you use with, the file object returned by open() is only abailable inside-
#-the with block that contains it
#you can store the file's lines in a list inside the block and then work with that list instead
with open(filename) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())

#readlines() method takes each line from the file and stores it in a list
    #then we used a for loop to print each line

#now let's try to get the full value of pi in one string
pi_string = ""  #creating a string to append to like a list
for line in lines:
    pi_string += line.strip()  #we use regular strip() because spaces are not to one side

print(pi_string)
print(len(pi_string))



#Wrtiting to a File

#to write to a file, call the open() method with a second argument telling python-
#-that you want to write to the file

#here we will write a messsage and store it in a file instead of printing it
filename2 = "programming.txt"
with open(filename2, "w") as file_object:
    file_object.write("I love programming.\n")
#the open() call in this example has two arguments
    #1st argument is the file we want to open
    #2nd argument "w" tells python we want to open the file in Write Mode

#You can open a file in three modes:
    #read mode "r"
    #write mode "w"
    #append mode "a"
    #read and write "r+"
#if you omit the mode argument, Python will open in read-only mode by default

#the open() function automatically creates the file you're writing to if it doesn't already exist
#be careful opening a file in write mode ("w") because python will overwrite it

#the write() function doesn't add newlines to text you write
    #so if you write more than line without including \n, it may not format correctly
#essentially remember to use \n if using write()
    file_object.write("Shoutout to coding \n")
    
#Appending to a File
    #Append Mode is useful for adding content without writing over existing content
    #you can write to the file using write(), similar to Write Mode
with open(filename2, "a") as file_object:
    file_object.write("I also love typing on the computer. \n")
    file_object.write("Make apps and use them on the computer. \n")

#continued in crash course ch10-2 notes
