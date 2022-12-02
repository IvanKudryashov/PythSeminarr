# По кругу стоят n человек. Ведущий посчитал m человек по кругу, начиная с первого. При этом каждый из тех, кто 
# участвовал в этом счете, получил по одной монете, остальные получили по две монеты. Далее человек, на котором 
# остановился счет, отдает все свои монеты следующему по счету человеку, а сам выбывает из круга. Процесс 
# продолжается с места остановки аналогичным образом до последнего человека в круге. Составьте алгоритм, который проводит эту игру.
people = int(input('Кол-во человек: '))
dropped = int(input('Через какое число считаем: '))
print('Значит, выбывает каждый', dropped, 'человек.')
people_list = list(range(1, people + 1))
out = 0
 
for _ in range(people - 1):
    print('\nТекущий круг людей', people_list)
    start_count = out % len(people_list)
    out = (start_count + dropped - 1) % len(people_list)
    print('Начало счёта с номера', people_list[start_count])
    print('Выбывает человек под номером', people_list[out])
    people_list.remove(people_list[out])
 
print('\nОстался человек под номером', *people_list)

money = 0
while (people != 1):
    if (people > dropped):
        money += dropped + (people - dropped) * 2        
    else:
        money += people       
    people -=1 

print(f'Количество монет -> {money}')