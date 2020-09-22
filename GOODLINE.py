def keyFunc(item):
   return item[1]

print('Введите строку')
str = str(input())

#УРОВЕНЬ 1

print('--СЛОВА ИЗ СТРОКИ--')
a = str.split(' ') #преоьразование строки разделяя ее на отдельные слова
for i in range(len(a)):
    print(a[i])

# УРОВЕНЬ 2

print('--ОТСОРТИРОВАННЫЕ--')
a.sort() # сортировка слов в списке
aSort = a
for i in range(len(aSort)):
    print(aSort[i])

# УРОВЕНЬ 3

print('--ТЕПЕРЬ ОСТАЛИСЬ ТОЛЬКО УНИКАЛЬНЫЕ--')
i = 0
while i < len(aSort)-1:   #цикл для вывода уникальных слов
    if aSort[i] != aSort[i+1]:
        print(aSort[i])
    i+=1
print(aSort[-1]) #вывод последнего символа отсортированного массива

# УРОВЕНЬ 4

print('--Количество повторений слов в списке--')
i = 0
k = 0
while i < len(aSort)-1:   #цикл для вывода уникальных слов
    if aSort[i] != aSort[i+1]:
        print(aSort[i],' ',k+1)
        k = 0
    else: k +=1
    i+=1
print(aSort[-1],' ', k+1) #вывод последнего символа отсортированного массива, он всегда ункален после сортировки

#5 УРОВЕНЬ
print('5 УРОВЕНЬ')
A =[] #пустой список
i = 0
k = 0
while i < len(aSort)-1:   #цикл для вывода уникальных слов
    if aSort[i] != aSort[i+1]:
        # print(aSort[i],' ',k+1)
        A.append([aSort[i],k+1])#Добавление вложенного списка в список(Создаем двумерный список)
        k = 0
    else: k +=1
    i+=1
A.append([aSort[-1],k+1]) #добавление в конец двумерного массиваэлементов

A.sort(key=keyFunc, reverse = True) #сортировка по числу, по убыванию

# Сортировка по убыванию алфавита если количество повторений равно
for i in range(len(A)-1):
    if A[i][1] == A[i+1][1]:
        f1 = i
        if A[i][0] < A[i+1][0]:
           reserv = A[i][0]
           A[i][0] = A[i+1][0]
           A[i+1][0] = reserv
        k+=1

for i in range(len(A)):
    print(A[i])