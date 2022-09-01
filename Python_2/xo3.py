# Игра "КРЕСТИКИ-НОЛИКИ"

# ********************************************************
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# ********************************************************
import random
# ********************************************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# ********************************************************
def displayBoard(board):
    # Эта функция выводит на экран игровое поле,
    # клетки которого будут заполнятся

    # "board" - это список в котором хранится 10 строк
    # для прорисовки игрового поля (индекс 0 ингрориуется)

    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-+-+-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-+-+-')
    print(board[1]+'|'+board[2]+'|'+board[3])

def inputPlayerLetter():
    # предложение игроку ввести букву, которую он выбирает
    letter = ''
    while not (letter=='X' or letter=='O'):
        print('''    Выберите "Х" или "О".
    Для выбора введите соответственно "Х" или "О" 
    на английской раскладке.''')

        letter = input().upper()

    if letter == 'X':
        return ['X','O']
    else:
        return ['O','X']

def whoGoesFirst():
    # Случайным образом выбираем кто будет ходить первым
    if random.randint(0,1) == 0:
        return 'Компьютер'
    else:
        return 'Человек'



# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

print(whoGoesFirst())