import csv
from string import ascii_lowercase as alc
from string import ascii_uppercase as auc

def assign_aplhabets():
    lowercase_values = {}
    uppercase_values = {}

    for index, aplhabets in enumerate(alc):
        lowercase_values[aplhabets] =  index + 1

    for index, aplhabets in enumerate(auc):
        uppercase_values[aplhabets] = index + 27

    return lowercase_values, uppercase_values

def sum_items():
    lowercase_values, uppercase_values = assign_aplhabets()
    sum_common_string = 0

    for items in csv.reader(open('rucksack_items.txt')):
        value = items[0]
        firstpart, secondpart = value[:len(value)//2], value[len(value)//2:]

        com_str = ''.join(set(firstpart).intersection(secondpart))
    
        if com_str.isupper():
            sum_common_string = sum_common_string + uppercase_values[com_str]
        elif com_str.islower():
            sum_common_string = sum_common_string + lowercase_values[com_str]
        else:
            raise ValueError('Invalid input')
    return sum_common_string

def sum_badges():
    lowercase_values, uppercase_values = assign_aplhabets()
    sum_badges = 0
    value = []
    
    for items in csv.reader(open('rucksack_items.txt')):
        value.append(items[0])

    for i in range(0, len(value), 3):
        first_group_member = value[i]
        second_group_member = value[i+1]
        third_group_member = value[i+2]

        com_str = ''.join(set(first_group_member).intersection(second_group_member).intersection(third_group_member))
        
        if com_str.isupper():
            sum_badges = sum_badges + uppercase_values[com_str]
        elif com_str.islower():
            sum_badges = sum_badges + lowercase_values[com_str]
        else:
            raise ValueError('Invalid input')
    return sum_badges
        

print('Sum of priorities of items in rucksack', sum_items())
print('Sum of priorities of team badges', sum_badges())