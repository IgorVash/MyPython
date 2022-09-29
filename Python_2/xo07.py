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

def makeMove(board,letter,move):
    board[move] = letter

def isWinner(bo,le):
    # Учитывая заполнение игрового поля и буквы игрока,
    # эта функция возвращает True, если игрок выиграл

    # Мы будем использовать "bo" вместо "board"
    # и "le" вместо "letter" для удобства, чтобы
    # меньше писать

    return ((bo[7]==le and bo[8]==le and bo[9]==le) or # верхняя строка
    (bo[4]==le and bo[5]==le and bo[6]==le) or # средняя строка 
    (bo[1]==le and bo[2]==le and bo[3]==le) or # нижняя строка
    (bo[7]==le and bo[4]==le and bo[1]==le) or # левый столбец
    (bo[8]==le and bo[5]==le and bo[2]==le) or # центральный столбец
    (bo[9]==le and bo[6]==le and bo[3]==le) or # правый столбец
    (bo[7]==le and bo[5]==le and bo[3]==le) or # диагональ слева-направо
    (bo[9]==le and bo[5]==le and bo[1]==le))   # диагональ справа-налево
    
def getBoardCopy(board):
    # когда ходит компьютер, бывает необходимо модифицировать
    # копию игрового поля, не затрагивая основное игровое поле
    # эта функция как раз и создает копию и возвращает его
    boardCopy = []
    for i in board:
        boardCopy.append(i)
    return boardCopy

def isSpaceFree(board,move):
    # функция проверяет свободна ли ячейка игрового поля
    # и можно ли туда сделать ход. Возвращает True, если
    # ход можно сделать и False, если нельзя
    return board[move] == ' '

def getPlayerMove(board):
    # функция предлагает игроку сделать ход и принимает
    # от него номер ячейки, куда он делает ход
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board,int(move)):
        print('Ваш следующий ход? Введите номер ячейки. (1-9)')
        move = input()
    return int(move)

# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

#board = [' ',' ',' ',' ',' ',' ',' ',' ',' ',' ']
board = [' ']*10
board[5] = 'O'
displayBoard(board)
m = getPlayerMove(board)
makeMove(board,'X',m)
displayBoard(board)