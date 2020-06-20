def get_percent(combos):
    for combo in combos:
        count = 0
        percentage_file = open('Hand_Percentages', 'w')
        for i in range(0, 1326):
            list_combo = list(combo)
            new = ''.join(list_combo)
            num1 = 0 + (12*count)
            num2 = 12 + (12*count)
            count += 1
            doc_title = new[num1:num2]
            wl = open(doc_title, 'r')
            wl2 = wl.read()
            win_count = wl2.count('Win')
            loss_count = wl2.count('Loss')
            chop_count = wl2.count('Tie')
            percentage = (win_count/(win_count + loss_count + chop_count)) * 100
            percentage_file.write(doc_title + ': ' + str(percentage) + '\n')


read_combos = open('combos.txt', 'r')
get_percent(read_combos)

