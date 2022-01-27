a = [3, 10, -1]
a.append(1)
#sort puts items in list from high to low
a.sort()
#you can mix types within a single list
a.append("hello")
#can put other lists into lists
a.append([1, 2])
#.pop() function will remove the last item in a list
a.pop()
a.pop()
print(a)

#index starts at 0 in python. a[0] will call the first item
#[-1] will call the last item in a list

a[0] = 100 #this bit of code replaces index 0 in the list with 100
print(a)

b = ["banana", "apple", "microsoft"]
#can we change the order of this list of strings? yes
temp = b[0]
#defining temp, new temporary variable. referring to "banana" at index 0
b[0] = b[2] #now saying first index should refer to what the third item refers to
b[2] = temp #third compartment now refers to what temp refers to
#list now reads ["microsoft", "apple", "banana"]
print(b)
#shortcut for this: b[0], b[2] = b[2], b[0]
