import math
import random
import os
import re

os.system("cls")

# Домашнее задание Семинар 5* (сдавать только к семинару 5!)

# Задача 26
# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

# def degree(A, B):
#     if B == 0:
#         return 1
#     elif B == 1:
#         return A
#     else:
#         return A * degree(A, B - 1)

# Num_1 = int(input ("Введите число, которое требуется возвести в степень: "))
# Num_2 = int(input ("Введите степень, в которую требуется возвести число: "))

# print (f"{Num_1} в {Num_2} степени = {degree(Num_1, Num_2)}")

#####################################################################

# Задача 28
# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. Из всех арифметических операций
# допускаются только +1 и -1. Также нельзя использовать циклы.

# def sumir(a, b):
#     if a == 0:
#         return b
#     elif b == 0:
#         return a
#     else:
#         return 1 + (sumir (a, b - 1))

# Num_1 = int(input ("Введите 1 число: "))
# Num_2 = int(input ("Введите 2 число: "))

# print(f"Сумма чисел {Num_1} и {Num_2} = {sumir(Num_1, Num_2)}")

##############################################################################

# Задача 101
# Вычислить число π c заданной точностью d

# Пример:
# при d = 0.001, π = 3.141   0.00000000001 ≤ d ≤ 0.1

# d = float(input("Введите d (0.00000000001 ≤ d ≤ 0.1): "))
# if d >= 0.1 or d <= 0.00000000001:
#     print('Условие не выполнено: 0.1 ≤ d ≤ 0.00000000001')
#     quit()
# else:
#     print('Число Пи в библиотеке math =', math.pi)

#     count = 2

#     while d < 1:
#         d = d * 10
#         count += 1

#     print('Число Пи с заданной точностью =', str(math.pi)[:count])

##############################################################################

# Задача 102
# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

N = int(input("Введите натуральное число: "))
if N <= 0:
    print (f'Число {N} не является натуральным числом')
    quit()
elif N == 1:
    print('У числа 1 нет простых множителей')
else:
    m = []

    for i in range(1, N + 1):
        if i % 2 == 0:
            m.append(i)
    print(m)

##############################################################################

# Задача 103
# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл file1.txt многочлен степени k.

# Здесь же:
# Задача 104
# Даны два файла file1.txt и file2.txt, в каждом из которых находится запись многочлена (полученные в результате работы
# программы из задачи 103). Необходимо сформировать файл file_sum.txt, содержащий сумму многочленов.

# Пример:  k=2

# Возможные варианты многочленов:
# 2*x*x + 4*x + 5 = 0
# x*x + 5 = 0
# 10*x*x = 0


def polynomial(k, n):
    rand1 = []
    for i in range(2):
        # Программа работает и для отрицательных коэффициентов при Х
        rand1.append(random.randint(0, 100))

    if k == 0:
        return "Не, так не пойдет. Нужно больше"

    elif k == 1:
        if rand1[0] == 1:
            if rand1[1] > 0:
                return f"+ x + {rand1[1]} = 0"
            elif rand1[1] == 0:
                return f"+ x = 0"
            else:
                return f"+ x {rand1[1]} = 0"
        elif rand1[0] == -1:
            if rand1[1] > 0:
                return f"- x + {rand1[1]} = 0"
            elif rand1[1] == 0:
                return f"- x = 0"
            else:
                return f"- x {rand1[1]} = 0"
        elif rand1[0] == 0:
            if rand1[1] > 0:
                return f"+ {rand1[1]} = 0"
            elif rand1[1] == 0:
                return f" = 0"
            else:
                return f"+ x = 0"

        else:
            if rand1[0] > 0:
                if rand1[1] == 0:
                    return f"+ {rand1[0]} * x = 0"
                else:
                    if rand1[1] > 0:
                        return f"+ {rand1[0]} * x + {rand1[1]} = 0"
                    else:
                        return f"+ {rand1[0]} * x {rand1[1]} = 0"
            else:
                if rand1[1] == 0:
                    return f"{rand1[0]} * x = 0"
                else:
                    if rand1[1] > 0:
                        return f"{rand1[0]} * x + {rand1[1]} = 0"
                    else:
                        return f"{rand1[0]} * x {rand1[1]} = 0"

    else:
        if n <= k:
            if rand1[0] >= 0:  # проверка первой итерации: если знак +, то его вначале не пишем
                # проверка на коэффициент 1 (если = 1, то его не пишем перед х)
                if rand1[0] == 1:
                    return f"x ^ {k} {polynomial(k-1, n)}"
                # проверка на коэффициент 0 (если = 0, то данную итерацию пропускаем)
                elif rand1[0] == 0:
                    return f"{polynomial(k-1, n)}"
                else:
                    if rand1[0] == 0:
                        return f"{polynomial(k-1, n)}"
                    else:
                        return f"{rand1[0]} * x ^ {k} {polynomial(k-1, n)}"

            else:
                return f"{rand1[0]} * x ^ {k} {polynomial(k-1, n)}"
        else:
            if rand1[0] > 0:
                if rand1[0] == 1:
                    return f"+ x ^ {k} {polynomial(k-1, n)}"
                else:
                    return f"+ {rand1[0]} * x ^ {k} {polynomial(k-1, n)}"
            elif rand1[0] == 0:
                return f"{polynomial(k-1, n)}"
            else:
                if rand1[0] == -1:
                    return f"- x ^ {k} {polynomial(k-1, n)}"
                else:
                    return f"{rand1[0]} * x ^ {k} {polynomial(k-1, n)}"


def getPolin(itog):  # Парсинг
    maxDeg = 0
    polinom1 = itog.strip(' ')[0:-4].replace(' ', '').split('+')
    pDict = dict()
    for item in polinom1:
        degree = 0
        if len(item.split('^')) > 1:  # Длина по разделителю (тут либо 1, либо 2)
            degree += int(item.split('^')[1])
            if maxDeg < degree:
                maxDeg = degree
        index = 0
        k = ''
        while index < len(item):
            if item[index].isdigit():
                k += item[index]
                index += 1
                continue
            if item[index] == 'x' or item[index] == '*':
                if degree == 0:
                    degree = 1
                break
        if k == '':
            k = '1'
        pDict[degree] = int(k)
    return pDict, maxDeg


def SumPolin(itog, Pars1, Pars2):  # Функция сложения
    polinom2 = itog.strip(' ')[0:-4].replace(' ', '')
    polinom1 = re.split(r'\+|\*', polinom2)
    polinom1.reverse()
    num1 = []
    num = ''
    for char in polinom1:  # Отделение цифр от х и степеней
        if char.isdigit():
            num = num + char
        else:
            if num != '':
                num1.append(int(num))
                num = ''
    if num != '':
        num1.append(int(num))

    Dict1 = Pars1[0]
    Dict2 = Pars2[0]
    for k in Dict1.keys() & Dict2.keys():  # Непосредственное сложение
        SumK = Dict1[k] + Dict2[k]
        for i in Dict1.keys():
            if Dict1[i] == num1[k]:
                Dict1[i] = SumK

    polynS = ''
    for k in Dict1.keys():
        if k >= 2:
            polynS = polynS + f'{Dict1[k]} * x ^ {k} + '
        elif k == 1:
            polynS = polynS + f'{Dict1[k]} * x + '
        elif k == 0:
            polynS = polynS + f'{Dict1[k]} = 0'
    return polynS


k = int(input("Задайте натуральную степень 1 полинома: "))
s = int(input("Задайте натуральную степень 2 полинома: "))

n = k  # первое вхождение в цикл для первой итерации
itog1 = polynomial(k, n)
print(itog1)

f = open('file1.txt', 'w+')  # Очистка файла
f.seek(0)
f.close()

data1 = open('file1.txt', 'a')
data1.writelines(itog1)
data1.close()

n = s  # первое вхождение в цикл для первой итерации во втором многочлене
itog2 = polynomial(s, n)
print(itog2)

f = open('file2.txt', 'w+')  # чтение из файла
f.seek(0)
f.close()

data1 = open('file2.txt', 'a')
data1.writelines(itog2)
data1.close()

# Pars1 = getPolin(itog1) #Парсинг ------------------------Сложение многочленов непосредственно без чтения из файлов
# Pars2 = getPolin(itog2)

# dictPars1 = Pars1[0] # Получение значений словаря без степени

# dictPars2 = Pars2[0] # Получение значений словаря без степени

# print ("Cумма двух многочленов равна: ")
# if Pars1[1] >= Pars2[1]:
#     print (SumPolin(itog1, Pars1, Pars2))
# else:
#     print (SumPolin(itog2, Pars2, Pars1))

with open('file1.txt') as f:
    s1 = f.read()

with open('file2.txt') as f:
    s2 = f.read()

Pars1 = getPolin(s1)
Pars2 = getPolin(s2)

dictPars1 = Pars1[0]  # Получение значений словаря без степени

dictPars2 = Pars2[0]  # Получение значений словаря без степени

print("Cумма двух многочленов равна: ")
if Pars1[1] >= Pars2[1]:
    itogsum = SumPolin(s1, Pars1, Pars2)
    print(itogsum)
else:
    itogsum = SumPolin(s2, Pars2, Pars1)
    print(itogsum)

f = open('file_sum.txt', 'w+')
f.seek(0)
f.close()

data3 = open('file_sum.txt', 'a')
data3.writelines("Sum polinoms = ")
data3.writelines(itogsum)
data3.close()
