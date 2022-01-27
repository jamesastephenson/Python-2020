a = ['apple', 'banana', 'republic']
for element in a:
    print(element)

#the below code is better for when the index number matters
for i in range(len(a)): #0, 1, 2
    for j in range(i+1):
        #i = 0 -> j = 0
        #i = 1 -> j = 0, 1
        #i = 2 -> j = 0, 1, 2
        print(a[i])

#dictionaries in python are essentially a lookup table
    #key value pairs, are made up of keys (usually a string) and-
    #a value that it is assigned to
#curly braces define dictionaries (or you can use dict() )
d = {}
#d = {'George':24, 'Tom': 32)
#the string marked with a colon makes a key value pair, each separated by commas
d['George'] = 24
d['Tom'] = 32
d['Jenny'] = 16
#our dictionary now has 3 key value pairs
print(d['George'])
print(d['Tom'])

#we can change the value of a key value pair by setting it equal again
d['Jenny'] = 20

#most commonly, keys are strings or numbers
#you can mix types as well
d[10] = 100
print(d[10])


#how to iterate over key-value pairs?
for key, value in d.items():
    print('Key: ')
    print(key)
    print('Value: ')
    print(value)
    print('')
