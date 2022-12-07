def max_calories():
    with open('2022_Challenge_1/calorie.txt','r') as input_file:
        data_str = input_file.read()
        data_array = data_str.split('\n\n') # Split on all instances of double new lines

        sum_calories = []
        for values in data_array:
            values = values.split('\n')
            total_calories = 0
            for calories in values:
                total_calories = total_calories + int(calories)
            sum_calories.append(total_calories)
        return max(sum_calories)

def calories_three_elves():
    with open('2022_Challenge_1/calorie.txt','r') as input_file:
        data_str = input_file.read()
        data_array = data_str.split('\n\n') # Split on all instances of double new lines

        sum_calories = []
        for values in data_array:
            values = values.split('\n')
            total_calories = 0
            for calories in values:
                total_calories = total_calories + int(calories)
            sum_calories.append(total_calories)

        sum_calories.sort(reverse=True)
        return(sum_calories[0]+sum_calories[1]+sum_calories[2])

print('Maximum calorie by an elf:', 
      max_calories())

print('Maximum calorie by three elves:',
      calories_three_elves())



        