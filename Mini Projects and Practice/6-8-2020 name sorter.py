name_list = ['Andy', 'Andrew', 'Abby', 'Barry', 'Becky', 'Clyde', 'Clarissa', 'Kenan', 'Jacob', 'John', 'Jenn', 'Stephen', 'Zoe', 'Jeff', 'Carol', 'Charlie', 'Chett', 'Chazz', 'Jaden']

searched_letter = input('Please enter a letter to search: ')
def name_finder(first_letter):
    found_name_list = []
   
    for name in name_list:
        if name[0].lower() == first_letter.lower():
            found_name_list.append(name)
        elif name[0].lower() != first_letter.lower():
            not_in_list = 'There are no names that start with that character'
            return not_in_list
        else:
            error_string = 'That is not a letter!'
            return error_string
    return found_name_list

print(name_finder(searched_letter))
