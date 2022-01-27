total = 0
for i in range (1, 5):
    total += i
print(total)

total2 = 0
j = 1 #we need to define j outside of the loop for a while loop
while j < 5:
    total2 += j
    j += 1
print(total2)

#while loops are useful when you don't know how many loops are needed beforehand

given_list = [5, 4, 4, 3, 1, -2, -3, -5]
#want to iterate only the positive numbers in given_list
total3 = 0
i = 0
while given_list[i] > 0:
    total3 += given_list[i]
    i += 1
#this loop will only iterate through the positive items in the list-
#-because the while loop is only set for items > 0
#NOTE: this loop would not work if the list was all positive numbers-
#-would continue to iterate out of the range
    #adding an additional condition to the while loop (i < len(given_list)) would fix
print(total3)

given_list2 = [5, 4, 4, 3, 1, -2, -3, -5]
total4 = 0
for element in given_list2:
    if element <= 0:
        break
    total4 += element
print(total4)
#the break statement prevents us from indexing the elements with negative numbers
#break statement works the same in while loops

total5 = 0
i = 0
while True: #while True is here so that it iterates constantly until the break
    total5 += given_list2[i]
    i += 1
    if given_list[i] <= 0:
        break
print(total5)

given_list3 = [7, 5, 4, 4, 3, 1, -2, -3, -5, -7]
#add all of the negative numbers using a why loop
total6 = 0
i = -1
while given_list3[i] < 0:
    total6 += given_list3[i]
    i -= 1
print(total6)
#for this solution, we counted backwards in the list
