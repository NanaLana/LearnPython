# Посчитать и вывести средний балл по всей школе.
# Посчитать и вывести средний балл по каждому классу.
school = [
    {'school_class': '4a', 'scores': [4, 4, 4, 5, 3]}, #4.0
    {'school_class': '5a', 'scores': [3, 5, 4, 5, 5]}, #4.4
    {'school_class': '6a', 'scores': [5, 3, 3, 5, 3]}] #3.8
total_summ = 0
total_counter = 0
for line in school:
    scores = line['scores'] #[4, 4, 4, 5, 3]
    total_counter = total_counter + 1
    scores_summ = 0
    count = 0
    for mark in scores:
        scores_summ = scores_summ + mark
        count = count + 1
    class_middle_summ = scores_summ/count
    total_summ = total_summ + class_middle_summ
    print(line['school_class']+ ': ' + str(class_middle_summ))
all_school = total_summ/total_counter     
print("Средний балл по всей школе: " +  str(all_school))
