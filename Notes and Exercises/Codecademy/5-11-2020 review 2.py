a = ['banana', 'apple', 'microsoft']
for element in a:
    print(element)
    print(element)

b = [20, 10, 5]
total = 0
for e in b:
    total += e
print(total)

c = list(range(1,5))
print(c)

total2 = 0
for i in range(1,5):
    total2 += i
print(total2)

d = list(range(1, 8))

total3 = 0
for i in d:
    if i % 3 == 0:
        total3 += i
print(total3)

#Can you compute all the multiples of 3 and 5 that are less than 100?
multiples_list = []
for i in range(1,100):
    if (i % 3 == 0) or (i % 5 == 0):
        multiples_list.append(i)
print(multiples_list)
