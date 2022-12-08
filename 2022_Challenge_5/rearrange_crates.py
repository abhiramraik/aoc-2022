import csv


pair_list = []
for pairs in csv.reader(open('2022_Challenge_5/crates_position.txt')):
    pair_list.append(pairs)

print(pair_list)
