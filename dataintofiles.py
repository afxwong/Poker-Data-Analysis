import csv
from itertools import combinations

f = open('trial4.csv')
csv_f = csv.reader(f)

deck = ['AH', '2H', '3H', '4H', '5H', '6H', '7H', '8H', '9H', 'TH', 'JH', 'QH', 'KH',
        'AC', '2C', '3C', '4C', '5C', '6C', '7C', '8C', '9C', 'TC', 'JC', 'QC', 'KC',
        'AS', '2S', '3S', '4S', '5S', '6S', '7S', '8S', '9S', 'TS', 'JS', 'QS', 'KS',
        'AD', '2D', '3D', '4D', '5D', '6D', '7D', '8D', '9D', 'TD', 'JD', 'QD', 'KD']
'''
comb = combinations(deck, 2)
for i in list(comb):
    a = list(i)
    combs = open('combos.txt', 'a')
    combs.write(str(a))
    combs.close()
'''


def check_if_string_in_file(file_name, string_to_search):
    # Open the file in read only mode
    with open(file_name, 'r') as read_obj:
        # Read all lines in the file one by one
        for line in read_obj:
            # For each line, check if line contains the string
            if string_to_search in line:
                return True
    return False


for row in csv_f:
    combs = open('combos.txt', 'r')
    print(row[0])
    if check_if_string_in_file('combos.txt', row[0]):
        new_file = open(row[0], 'a')
        new_file.write(row[1])
    else:
        unmatched_expanded = list(row[0])
        temp = unmatched_expanded[1:5]
        unmatched_expanded[1:5] = unmatched_expanded[7:11]
        unmatched_expanded[7:11] = temp
        swapped = ''.join(unmatched_expanded)
        print(swapped)
        if check_if_string_in_file('combos.txt', swapped):
            new_file = open(swapped, 'a')
            new_file.write(row[1])

combs.close()