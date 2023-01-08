# 1. A. Задана натуральная степень k. Сформировать случайным образом 
# список коэффициентов (значения от 0 до 100) многочлена и записать в 
# файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 
# или x² + 5 = 0 или 10*x² = 0


# def mnh(k):
#     mn = []
#     ravn = ' = 0'
#     key = []
#     my_string = []
#     import random
#     x = '+'
#     for i in range(k+1):
#         mn.append(random.randint(0,101))
#         key.append(k -i)
#         if mn[i] != 0:
#             my_string.append(f'{mn[i]}X^{key[i]}')
#             my_list = x.join(my_string)
#     my_list = my_list.replace('X^0', '').replace('^1', '').replace('1X', 'X')
#     my_list += ravn
#     return my_list
# k = int(input('Введите натуральную степень K: '))   
# mnh(k)
# print(mnh(k))
# data1 = open('seminar.py\data1.txt', 'w')
# data1.writelines(mnh(k))
# data1.close()
# data2 = open('seminar.py\data2.txt', 'w')
# data2.writelines(mnh(k))
# data2.close()



# B. Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.


# mn1 = []
# mn2 = []
# path = 'seminar.py\data1.txt'
# data1 = open(path, 'r')
# for line in data1:
#     mn1.append(str(line))
# data1.close()
# path = 'seminar.py\data2.txt'
# data2 = open(path, 'r')
# for line in data2:
#     mn2.append(line)
# data2.close()
# print(*mn1)
# print(*mn2)
# mn1 = str(*mn1)
# mn2 = str(*mn2)

# def smn(string: str):
#     sum = {}
#     string = string.replace(' ', '').replace('=0', '').replace('+', ' ').split()
#     for item in string:
#         if item.find('X') == -1:
#             key = 0
#         elif item.find('^') == -1:
#             key = 1
#         else:  key = int(item.split('X^')[1])
#         if item.startswith('X'):
#             per = 1
#         else:  per = int(item.split('X')[0])
#         sum[key] = per
#     return sum
# smn(mn1)
# m1 = smn(mn1)
# smn(mn2)
# m2 = smn(mn2)

# m3 ={}
# keys = set()
# for key in m1:
#     keys.add(key)
# for key in m2:
#     keys.add(key)
# for key in keys:
#     m3[key] = m1.get(key, 0) + m2.get(key, 0)  
# sum = []
# sum1 = []
# ks = []
# x = ' + '
# ravn = ' = 0'
# for k in sorted(m3.keys(), reverse=True):
#     ks.append(k)  
# for key in ks:
#     sum.append(f'{m3[key]}X^{key}')
#     sum1 = x.join(sum)
#     sum1 = sum1.replace('X^0', '').replace('^1', '')
#     sum1 += ravn
# print(sum1)
# datas = open('seminar.py\datas.txt', 'w')
# datas.writelines(sum1)
# datas.close()



# НЕОБЯЗАТЕЛЬНОЕ, ДОПОЛНИТЕЛЬНОЕ ЗАДАНИЕ:
# Расширить значение коэффициентов до [-100..100]

# k = int(input('Введите натуральную степень K: '))
# mn = []
# key = []
# my_string = []
# import random
# x = ' + '
# for i in range(k+1):
#     mn.append(random.randint(-100,101))
#     key.append(k - i)
#     my_string.append(f'{mn[i]}X^{key[i]}')
#     my_list = x.join(my_string)
# my_list1 = my_list.replace('X^0', '').replace('^1', '').replace('+ -', '- ')
# print(my_list1, end=' = 0')

# def mnh(k):
#     mn = []
#     ravn = ' = 0'
#     key = []
#     my_string = []
#     import random
#     x = ' + '
#     for i in range(k+1):
#         mn.append(random.randint(-100,101))
#         key.append(k -i)
#         if mn[i] != 0:
#             my_string.append(f'{mn[i]}X^{key[i]}')
#             my_list = x.join(my_string)
#     my_list = my_list.replace('X^0', '').replace('^1', '')\
#         .replace('1X', 'X').replace('+ -', '- ')
#     my_list += ravn
#     return my_list
# k = int(input('Введите натуральную степень K: '))   
# mnh(k)
# print(mnh(k))