# a = int(input("Количество парт 1-ого кабинета: "))
# b = int(input("Количество парт 2-ого кабинета: "))
# c = int(input("Количество парт 3-го кабинета: "))
# s1 = (a + 1) // 2
# s2 = (b + 1) // 2
# s3 = (c + 1) // 2
# print(s1 + s2 + s3)


# i = int(input("Введите вагон от головы поезда:"))
# j = int(input("Введите номер вагона:"))
# if i == j:
#     print("Невозможно определить")
# else:
#     print(i+j-1)

# year = int(input("Введите год:"))
# if year % 4 == 0 and year % 100 != 0 or year % 400 == 0:
#     print ("yes") 
# else:
#     print ("No")


# if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
#     print('yes')
# else:
#     print('no')    


# ДОМАШНЯЯ РАБОТА

# Задача 2: Найдите сумму цифр трехзначного числа.

# i = int(input("Введите трехзначное число:"))
# n = i % 10 + i % 100 // 10 + i % 1000 // 100
# print (n)

# Задача 4: Петя, Катя и Сережа делают из бумаги журавликов. Вместе они 
# сделали S журавликов. Сколько журавликов сделал каждый ребенок, если 
# известно, что Петя и Сережа сделали одинаковое количество журавликов, а 
# Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?

# i = int(input("Введите общее количество журавликов, сделанное всеми детьми:"))
# x = i // 6
# print (x, 4*x, x)   

# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались
# за проезд и получали билет с номером. Счастливым билетом называют такой 
# билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. 
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6. 
# Вам требуется написать программу, которая проверяет счастливость билета.

# i = int(input("Введите номер билета из 6 цифр:"))
# a = i % 10 + i % 100 // 10 + i % 1000 // 100
# b = i % 10000 // 1000 + i % 100000 // 10000 + i % 1000000 // 100000
# if a == b:
#     print ("yes")
# else:
#      print ("No")


# Задача 8: Требуется определить, можно ли от шоколадки размером n × m долек 
# отломить k долек, если разрешается сделать один разлом по прямой между дольками 
# (то есть разломить шоколадку на два прямоугольника).

# n = int(input("Введите размер шоколадки n: "))
# m = int(input("Введите размер шоколадки m: "))
# k = int(input("Введите количество долек: "))
# if k < m * n and k % n == 0 or k % m == 0:
#     print ("yes")
# else:
#     print ("No")   
    




    # СЕМИНАР 2
    # 1. По данному целому неотрицательному n вычислите значение n!. 
    # N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 
    # Решить задачу используя цикл while
    # Input:       5
    # Output:    120

    # n = int(input("Введите число: "))
    # i = 2
    # result = 1
    # while i <= n:
    #     result *= i # result = result * i
    #     i += 1
    # print(f'{n}! = {result}')

    # 2. Дано натуральное число A > 1. Определите, каким по счету числом 
    # Фибоначчи оно является, то есть выведите такое число n, что φ(n)=A. 
    # Если А не является числом Фибоначчи, выведите число -1.
    # Input:     5
    # Output:  6

# n = int(input("Введите число: "))
# a0 = 0
# a1 = 1
# a2 = 0
# i = 2
# while a2 < n:
#     a2 = a1 + a0 # Для того чтобы найти 3-ое число, мы складываем 1-ое и 2-ое
#     a0 = a1 # Для того чтобы найти 4-ое число, мы складываем 2-ое и 3-е
#     a1 = a2
#     i += 1
# if a2 > n:
#     i = -1
# if i == -1:
#     print(i)
# else:
#     print(i)

# n = int(input("Ввдеите кол-во дней: "))
# count = 0
# max_days_count = 0
# for i in range(n):
#     x = int(input("Введите температуру сегодня: "))
#     if x > 0:
#         count += 1
#     else:
#         count = 0
    
#     if max_days_count < count:
#         max_days_count = count
# print(max_days_count)



# n = int(input("Ввдеите кол-во дней: "))
# count = 0
# max_days_count = 0
# # -10 30 -40 50 10 -20
# for i in range(n):
#     x = int(input("Введите температуру сегодня: "))
#     if x > 0:
#         count += 1
#     else:
#         if max_days_count < count:
#             max_days_count = count
#         count = 0


# print(max_days_count)


# адача №15. Общее обсуждение
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза

# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# n = int(input("Введите кол-во арбузов: "))
# # a = [43, 13, 0, -10, 35, 89]
# # 1 <= m <= 1000
# max_massa = 0
# min_massa = 1001
# for i in range(n):
#     x = int(input("Введите массу арбуза: "))
#     if x > max_massa:
#         max_massa = x

#     if x < min_massa:
#         min_massa = x
# print(min_massa, max_massa)

# ДЗ к СЕМИНАРУ 3

# Задача 16: Требуется вычислить, сколько раз встречается некоторое число X 
# в массиве A[1..N]. Пользователь в первой строке вводит натуральное число 
# N – количество элементов в массиве. В последующих  строках записаны N 
# целых чисел Ai. 
# Последняя строка содержит число X

# n = int(input("Введите количество элементов массива:"))
# array = []
# for i in range(n):
#     a = int(input("Введите элемент массива: "))
#     array.append(a)
# print(*array)
# x = int(input("Введите число, которое нужно найти в массиве: "))
# # Вариант 1 для себя
# # count = 0
# # for i in range(n):
# #     if  array[i] == x:
# #         count +=1
# # print(count)
# # Вариант 2 для сдачи
# print(sum([int(array[i] == x) for i in range(n)]))


# Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине 
# элемент к заданному числу X. Пользователь в первой строке вводит натуральное 
# число N – количество элементов в массиве. В последующих  строках записаны 
# N целых чисел Ai. 
# Последняя строка содержит число X

# n = int(input("Введите количество элементов массива:"))
# array = []
# for i in range(n):
#     a = int(input("Введите элемент массива: "))
#     array.append(a)
# print(*array)
# x = int(input("Введите число, которое нужно сравнить с элементами массива: "))
# min = abs(x - array[0])
# index = array[0]
# for i in range(1, len(array)):
#     y = abs(x - array[i])   
#     if y < min:
#         min = y
#         index = array[i]
# print(index)
    


#   *Задача 20: * В настольной игре Скрабл (Scrabble) каждая буква имеет 
#   определенную ценность. В случае с английским алфавитом очки распределяются так:
#   A, E, I, O, U, L, N, S, T, R – 1 очко; 
#   D, G – 2 очка; 
#   B, C, M, P – 3 очка; 
#   F, H, V, W, Y – 4 очка; 
#   K – 5 очков; 
#   J, X – 8 очков; 
#   Q, Z – 10 очков. 
#   А русские буквы оцениваются так: 
#   А, В, Е, И, Н, О, Р, С, Т – 1 очко; 
#   Д, К, Л, М, П, У – 2 очка; 
#   Б, Г, Ё, Ь, Я – 3 очка; 
#   Й, Ы – 4 очка; 
#   Ж, З, Х, Ц, Ч – 5 очков; 
#   Ш, Э, Ю – 8 очков; 
#   Ф, Щ, Ъ – 10 очков. 
#   Напишите программу, которая вычисляет стоимость введенного пользователем слова. 
#   Будем считать, что на вход подается только одно слово, которое содержит 
#   либо только английские, либо только русские буквы.

#   Пример: ноутбук  12      

eng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'}
rus = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
word = input('Введите слово: ').upper()
count = 0
for i in word:
    if i in 'qwertyuiopasdfghjklzxcvbnm'.upper():
        for j in eng:
            if i in eng[j]:
                count += j
    else:
        for j in rus:
            if i in rus[j]:
                count += j
print(count)







