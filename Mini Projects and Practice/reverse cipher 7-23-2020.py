#Reverse Cipher
#From Cracking Codes With Python (Al Sweigart)
#https://www.nostarch.com/crackingcodes

message = str(input("Enter a string to be reversed: \n>"))
test_message = "Three can keep a secret, if two of them are dead."
translated = ""

#i is message length - 1 to account for index values starting at 0
#in this example, i is referring to the last character in the string
i = len(message) - 1

#loop will continue until i value equals 0
while i >= 0:
    #concatenates the character at index i to our "translated" variable
    #because i is starting at the final index, it "translated" will be in reverse order as it loops
    translated = translated + message[i]
    i = i-1

print(translated)
