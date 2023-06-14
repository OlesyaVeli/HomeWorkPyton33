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

# eng = {1:'AEIOULNSTR', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JZ', 10:'QZ'}
# rus = {1:'АВЕИНОРСТ', 2:'ДКЛМПУ', 3:'БГЁЬЯ', 4:'ЙЫ', 5:'ЖЗХЦЧ', 8:'ШЭЮ', 10:'ФЩЪ'}
# word = input('Введите слово: ').upper()
# count = 0
# for i in word:
#     if i in 'qwertyuiopasdfghjklzxcvbnm'.upper():
#         for j in eng:
#             if i in eng[j]:
#                 count += j
#     else:
#         for j in rus:
#             if i in rus[j]:
#                 count += j
# print(count)
# 
# ДОМАШНЯЯ РАБОТА К СЕМИНАРУ 5
# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и 
# возводит число А в целую степень B с помощью рекурсии.

def degree(a, b):
    if b == 0:
        return 1
    return a * degree(a, b - 1)

a = int(input('Введите число: '))
b = int(input('Введите степень: '))
print(degree(a, b))