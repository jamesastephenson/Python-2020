#List Less Than Ten
#This program should take a list and print out all values less than 10
example_list = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#create a new list that we can append to
less_than_ten_list = []

#create a for loop to iterate through the list
for item in example_list:
    #if statement checks if the number is less than ten
    if item < 10:
        #if the number qualifies, we append it to our less_than_ten_list
        less_than_ten_list.append(item)
    #else statement tells us to ignore all nums less than 10
    else:
        continue
#print list
print(less_than_ten_list)
