import csv

def high_score():
    X = 1 # Rock
    Y = 2 # Paper
    Z = 3 # Scissors

    sum = 0
    for startegies in csv.reader(open('rps_challenge.txt')):
        value = startegies[0].split(' ')
        
        if value[0] == 'A' and value[1] == 'X':
            sum = sum + X + 3
        elif value[0] == 'A' and value[1] == 'Y':
            sum = sum + Y + 6
        elif value[0] == 'A' and value[1] == 'Z':
            sum = sum + Z + 0
    
        elif value[0] == 'B' and value[1] == 'X':
            sum = sum + X + 0
        elif value[0] == 'B' and value[1] == 'Y':
            sum = sum + Y + 3
        elif value[0] == 'B' and value[1] == 'Z':
            sum = sum + Z + 6
    
        elif value[0] == 'C' and value[1] == 'X':
            sum = sum + X + 6
        elif value[0] == 'C' and value[1] == 'Y':
            sum = sum + Y + 0
        elif value[0] == 'C' and value[1] == 'Z':
            sum = sum + Z + 3
        else:
            raise ValueError('Invalid input')
    return sum


def high_score_part_two():
    X1 = 0 # LOSE
    Y1 = 3 # DRAW
    Z1 = 6 # WIN

    X = A = 1 # Rock
    Y = B = 2 # Paper
    Z = C = 3 # Scissors

    sum = 0
    for startegies in csv.reader(open('rps_challenge.txt')):
        value = startegies[0].split(' ')
        
        if value[0] == 'A' and value[1] == 'X':
            sum = sum + Z + X1
        elif value[0] == 'A' and value[1] == 'Y':
            sum = sum + X + Y1
        elif value[0] == 'A' and value[1] == 'Z':
            sum = sum + Y + Z1
        elif value[0] == 'B' and value[1] == 'X':
            sum = sum + X + X1
        elif value[0] == 'B' and value[1] == 'Y':
            sum = sum + Y + Y1
        elif value[0] == 'B' and value[1] == 'Z':
            sum = sum + Z + Z1
        elif value[0] == 'C' and value[1] == 'X':
            sum = sum + Y + X1
        elif value[0] == 'C' and value[1] == 'Y':
            sum = sum + Z + Y1
        elif value[0] == 'C' and value[1] == 'Z':
            sum = sum + X + Z1
        else:
            raise ValueError('Invalid input')
    return sum

print('total score is :',high_score())
print('total score is 2nd task :',high_score_part_two())
