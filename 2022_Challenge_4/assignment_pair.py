import csv

pair_list = []
full_list = []
expanded_list = []
total_count = 0

for pairs in csv.reader(open('2022_Challenge_4/assignment_pair.txt')):
    pair_list.append(pairs[0].split('-'))
    pair_list.append(pairs[1].split('-'))

for pairs in pair_list: 
    for values in pairs:
        full_list.append(int(values))

for values in range (0, len(full_list), 2):
    if full_list[values] != full_list[values+1]:
        temp_list = [*range(full_list[values],full_list[values+1]+1)]
        expanded_list.append(temp_list)
    else:
        temp_list = [full_list[values]]
        expanded_list.append(temp_list)

for sets in range(0, len(expanded_list),2):
    if all(item in expanded_list[sets] for item in expanded_list[sets+1]):
        total_count +=1
    elif all(item in expanded_list[sets+1] for item in expanded_list[sets]):
        total_count +=1
print(total_count)


