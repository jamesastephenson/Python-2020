title = 'Umineko No Naku Koro Ni'

split_title = title.split()
n_titles = []

for word in split_title:
  if word[0] == 'N':
    n_titles.append(word)

print(n_titles)

random_list = [123, 0, 129837, 2, 4, 5, 6, 122, 144]

def total_sum(random_list):
  sum = 0
  for i in random_list:
    sum += i
  return sum
print(total_sum(random_list))
    
def first_3_numbers_sum(random_list):
  num_sum_3 = 0
  for i in random_list[0:3]:
    num_sum_3 += i
  return num_sum_3
print(first_3_numbers_sum(random_list))

title_len = len(title)
print(str(title_len))

split_title_len = len(split_title)
print(str(split_title_len))

def print_first_item(list):
  for item in list[0]:
    print(item)
    break

print_first_item(split_title)
print(title + ' ' + str(split_title))

