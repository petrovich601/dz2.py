# 1.Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит заданное количество конфет.
# Играют два игрока делая ход друг после друга.
# Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход.
# a) Добавьте игру против бота
# b) Подумайте как наделить бота 'интеллектом'


# def pl(i):
#     import random
#     if i == 1:
#         return int(input('1 игрок введите колличество конфет:  '))
#     else:
#         return int(input('1 игрок введите колличество конфет:  '))

# def pla(k):
#     import random
#     if k == 1:
#         return pl1
#     else:
#         return pl2

# import random
# pl1 = input('Введите имя игрока:  ')
# pl2 = input('Введите имя игрока:  ')
# igrok = random.randrange(1, 3)
# a = int(input('Введите колличество конфет:  '))
# if igrok == 1:
#     print('Первый ход делает: ', pl1)
#     x = 1
#     y = 2
# else:
#     print('Первый ход делает: ', pl2)
#     x = 2
#     y = 1
# while a > 0:
#     if a > 28:
#         igrok1 = pl(x)
#         a -= igrok1
#         if a > 28:
#             igrok2 = pl(y)
#             a -= igrok2
#         else:
#             print('Осталось ', a, 'шт, их забирает: ', pla(y), ', он победил')
#             a = 0
#     else:
#         print('Осталось ', a, 'шт, их забирает: ', pla(x), ', он победил')
#         a = 0


# a)

# def pl(i):
#     import random
#     if i != 1:
#         return random.randrange(1, 29)
#     else:
#         return int(input('Введите колличество конфет:  '))

# def pla(k):
#     import random
#     if k == 1:
#         return pl1
#     else:
#         return pl2

# import random
# pl1 = input('Введите имя игрока:  ')
# pl2 = 'PC'
# igrok = random.randrange(1, 3)
# a = int(input('Введите колличество конфет:  '))
# if igrok == 1:
#     print('Первый ход делает: ', pl1)
#     x = 1
#     y = 2
# else:
#     print('Первый ход делает: PC')
#     x = 2
#     y = 1
# igrok2 = random.randrange(1, 29)
# while a > 0:
#     if a > 28:
#         igrok1 = pl(x)
#         a -= igrok1
#         if a > 28:
#             igrok2 = pl(y)
#             a -= igrok2
#         else:
#             print('Осталось ', a, 'шт, их забирает: ', pla(y), ', он победил')
#             a = 0
#     else:
#         print('Осталось ', a, 'шт, их забирает: ', pla(x), 'он победил')
#         a = 0

# b)

# def pl(i):
#     import random
#     if i != 1:
#         if a > 56 or a == 29:
#             return random.randrange(1, 29)
#         elif a > 29:
#             return a - 29
#     else:
#         return int(input('Введите колличество конфет:  '))


# def pla(k):
#     import random
#     if k == 1:
#         return pl1
#     else:
#         return pl2

# import random
# pl1 = input('Введите имя игрока:  ')
# pl2 = 'PC'
# igrok = random.randrange(1, 3)
# a = int(input('Введите колличество конфет:  '))
# if igrok == 1:
#     print('Первый ход делает: ', pl1)
#     x = 1
#     y = 2
# else:
#     print('Первый ход делает: PC')
#     x = 2
#     y = 1
# while a > 0:
#     if a > 28:
#         igrok1 = pl(x)
#         a -= igrok1
#         print(a)
#         if a > 28:
#             igrok2 = pl(y)
#             a -= igrok2
#             print(a)
#         else:
#             print('Осталось ', a, 'шт, их забирает: ', pla(y), ', он победил')
#             a = 0
#     else:
#         print('Осталось ', a, 'шт, их забирает: ', pla(x), ', он победил')
#         a = 0


# 2. Создайте программу для игры в 'Крестики-нолики'
# НЕОБЯЗАТЕЛЬНО Добавить игру против бота с интеллектом

# maps = [1,2,3,
#         4,5,6,
#         7,8,9]
 
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])    
 
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 
# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
 
# game_over = False
# player1 = True
 
# while game_over == False:
 
#     print_maps()
 
#     if player1 == True:
#         symbol = "X"
#         step = int(input("Человек 1, ваш ход: "))
#     else:
#         symbol = "O"
#         step = int(input("Человек 2, ваш ход: "))
 
#     step_maps(step,symbol) 
#     win = get_result() 
#     if win != "":
#         game_over = True
#     else:
#         game_over = False
 
#     player1 = not(player1)        
       
# print_maps()
# print("Победил", win)


# a)
# maps = [1,2,3,
#         4,5,6,
#         7,8,9]
 
# victories = [[0,1,2],
#              [3,4,5],
#              [6,7,8],
#              [0,3,6],
#              [1,4,7],
#              [2,5,8],
#              [0,4,8],
#              [2,4,6]]
 
# def print_maps():
#     print(maps[0], end = " ")
#     print(maps[1], end = " ")
#     print(maps[2])
 
#     print(maps[3], end = " ")
#     print(maps[4], end = " ")
#     print(maps[5])
 
#     print(maps[6], end = " ")
#     print(maps[7], end = " ")
#     print(maps[8])
     
# def step_maps(step,symbol):
#     ind = maps.index(step)
#     maps[ind] = symbol
 
# def get_result():
#     win = ""
 
#     for i in victories:
#         if maps[i[0]] == "X" and maps[i[1]] == "X" and maps[i[2]] == "X":
#             win = "X"
#         if maps[i[0]] == "O" and maps[i[1]] == "O" and maps[i[2]] == "O":
#             win = "O"   
             
#     return win
 
# def check_line(sum_O,sum_X):
 
#     step = ""
#     for line in victories:
#         o = 0
#         x = 0
 
#         for j in range(0,3):
#             if maps[line[j]] == "O":
#                 o = o + 1
#             if maps[line[j]] == "X":
#                 x = x + 1
 
#         if o == sum_O and x == sum_X:
#             for j in range(0,3):
#                 if maps[line[j]] != "O" and maps[line[j]] != "X":
#                     step = maps[line[j]]
                 
#     return step
 
# def AI():        
#     step = ""
#     step = check_line(2,0)
#     if step == "":
#         step = check_line(0,2)        
#     if step == "":
#         step = check_line(1,0)           
#     if step == "":
#         if maps[4] != "X" and maps[4] != "O":
#             step = 5           
#     if step == "":
#         if maps[0] != "X" and maps[0] != "O":
#             step = 1           
#     return step
 
# game_over = False
# human = True
 
# while game_over == False:
#     print_maps()
#     if human == True:
#         symbol = "X"
#         step = int(input("Человек, ваш ход: "))
#     else:
#         print("Компьютер делает ход: ")
#         symbol = "O"
#         step = AI()
#     if step != "":
#         step_maps(step,symbol)
#         win = get_result()
#         if win != "":
#             game_over = True
#         else:
#             game_over = False
#     else:
#         print("Ничья!")
#         game_over = True
#         win = "дружба"
#     human = not(human)              
# print_maps()
# print("Победил", win)   




# 3. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.
# aaaaabbbcccc -> 5a3b4c
# 5a3b4c -> aaaaabbbcccc



# def encode(s):
#     encoding = ""
#     i = 0
#     while i < len(s):
#         count = 1
#         while i + 1 < len(s) and s[i] == s[i + 1]:
#             count = count + 1
#             i = i + 1
#         encoding += str(count) + s[i]
#         i = i + 1
#     return encoding

# string = input('Введите последовательность: ', )
# print(encode(string))

# def decode(s):
#     dec = ''
#     nam = ''
#     for i in s:
#         if i.isdigit():
#             nam += i
#         else:
#             dec += i * int(nam)
#             nam = ''
#     return dec

# string = input('Введите последовательность: ', )
# print(decode(string))
