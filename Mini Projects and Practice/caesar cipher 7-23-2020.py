#Caesar Cipher
#From Cracking Codes With Python (Al Sweigart)
#https://www.nostarch.com/crackingcodes

#import the code library
#import pyperclip

#The string to be encrypted/decrypted
message = "This is my secret message"

#The encryption/decryption key:
key = 13

#Whether the program encrypts or decrypts:
mode = "encrypt"

#Every possible symbol that can be encrypted:
SYMBOLS = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!?."

#Store the encrypted/decrypted form of the message (empty string for now):
translated = ""

for symbol in message:
    #note:only symbols in the SYMBOLS string can be encrypted/decrypted
    if symbol in SYMBOLS:
        #.find() method finds the first occurence of the specified value
        symbol_index = SYMBOLS.find(symbol)

        #perform the encryption/decryption
        if mode == "encrypt":
            translated_index = symbol_index + key
        elif mode == "decrypt":
            translated_index = symbol_index - key

        #handle wraparound if needed:
        if translated_index >= len(SYMBOLS):
            translated_index = translated_index - len(SYMBOLS)
        elif translated_index < 0:
            translated_index = translated_index + len(SYMBOLS)

        translated = translated + SYMBOLS[translated_index]
    else:
        #append the symbol without encrypting/decrypting:
        translated = translated + symbol

#output the translated string
print(translated)

