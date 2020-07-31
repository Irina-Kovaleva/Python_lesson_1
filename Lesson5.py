#Ex. 1
#Создать программно файл в текстовом формате, записать в него построчно данные,
#вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.

file = open('ex_1.txt','w')

text = str(input('Введите текст:'))

while text > "":

    file.write(text)
    text = str(input(''))

file.close()

#Ex. 2
#Создать текстовый файл (не программно), сохранить в нем несколько строк,
#выполнить подсчет количества строк, количества слов в каждой строке.

file = open('ex.txt','r')
lines = file.readlines()
ix = 0
for line in lines:
    w_num = line.count(' ') + 1
    print('Кол-во слов в %i-ой строке: %i' % (ix + 1, w_num))
    ix = ix + 1
print("Кол-во строк: %i" % ix)
file.close()

#Ex. 3
#Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
# пределить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
#Выполнить подсчет средней величины дохода сотрудников.

from functools import reduce

file = open('ex3.txt', 'r')
lines = file.readlines()

a = dict()
num = 0
s_summ = 0

print('Оклад менее 20000 у сотрудников:')
for line in lines:
    line = line.strip()
    list = line.split(' ')
    a[list[0]] = list[1]
    num = num + 1
    s_summ = s_summ + int(list[1])
    if int(list[1]) < 20000:
        print(list[0])

print('Средняя оклад: %2.f' % (s_summ / (num)))

file.close()

#Ex. 4
#Создать (не программно) текстовый файл со следующим содержимым:
#One — 1 Two — 2 Three — 3 Four — 4
#Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
# При этом английские числительные должны заменяться на русские.
# Новый блок строк должен записываться в новый текстовый файл.

file_1 = open('ex4_1.txt', 'r')
file_2 = open('ex4_2.txt', 'w')

dict = {'One':'Один', 'Two':'Два', 'Three':'Три', 'Four':'Четыре'}

lines = file_1.readlines()

for line in lines:
    list = line.split(' ')
    list[0] = dict.get(list[0])
    line = ' '.join(list)
    file_2.write(line)

file_1.close()
file_2.close()

#Ex. 5
#Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
# Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.

file = open('ex5.txt', 'r+')
list = '1 2 3 4 5 6'
file.write(list)
file.seek(0)
lines = file.read()
numbers = lines.split(' ')

summ = 0
i = 0
while i < len(numbers):
    summ = summ + int(numbers[i])
    i = i + 1

print(summ)
file.close()

#Ex. 6
#Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет и
# наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
# Важно, чтобы для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему.
# Вывести словарь на экран.

file = open('ex6.txt','r')
lines = file.readlines()

a = dict()

for line in lines:

    line = line.strip()
    line = line.replace('(l)','')
    line = line.replace('(pr)', '')
    line = line.replace('(lab)', '')
    line = line.replace(':', '')
    line = line.split(' ')

    summ = 0
    i = 0

    while i in range(len(line) - 1):
        summ = summ + int(line[i + 1])
        i = i + 1

    a[line[0]] = summ

print(a)
file.close()











