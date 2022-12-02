# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

a_list = [1, 15, -5, 4, 25, -6, 14, 1]
print(a_list)
rez = []
for i in a_list:
    rez.append(i)
    if i < 0:
        rez.append(0)
print(rez)
