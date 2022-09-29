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

def chooseRandomMoveFromList(board,movesList):
    # Возвращает допустимый ход, учитывая список возможных ходов
    # и список заполненных клеток.
    # Возвращает None, если больше нет допустимых ходов
    possibleMoves = []
    for i in movesList:
        if isSpaceFree(board,i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None

# Начало создания ИИ

def getComputerMove(board,computerLetter):
    # Учитывая заполнение игрого поля и символ компьютера,
    # определяем допустимы ход и возвращает его

    # Сначала определим сивол компьютера и человека
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    # дальше идет алгоритм для ИИ "Крестиков-Ноликов"

    # Сначала проверяем - победит ли ИИ, сделав следующий ход
    for i in range(1,10):
        # делаем копию игрового поля
        boardCopy = getBoardCopy(board)
        # проверяем свободна ли ячейка
        if isSpaceFree(board,i):
            # делаем ход в копии игрового поля
            makeMove(boardCopy,computerLetter,i)
            # проверяем выиграет ИИ сделав этот ход
            if isWinner(boardCopy,computerLetter):
                # если сделав ход ИИ выигрывает, возвращаем ход
                return i

    # теперь проверим, есть ли ход, который может сделать
    # человек и выиграть
    for i in range(1,10):
        # делаем копию игрового поля
        boardCopy = getBoardCopy(board)
        # проверяем свободна ли ячейка
        if isSpaceFree(board,i):
            # делаем ход в копии игрового поля
            makeMove(boardCopy,playerLetter,i)
            # проверяем выиграет человек сделав этот ход
            if isWinner(boardCopy,playerLetter):
                # если сделав ход человек выигрывает, делаем ход 
                # туда, чтобы блокировать ход человека
                return i

    # если нет ходов приводящих к победе компьютера или человека 
    # пытаемся занять один из улов, если есть свободные
    move = chooseRandomMoveFromList(board,[1,3,7,9])
    if move != None:
        return move

    # усли углы заняты, пробуем занять центр, если он свободен
    if isSpaceFree(board,5):
        return 5

    # делаем ход по одной из сторон
    return chooseRandomMoveFromList(board,[2,4,6,8])

# последняя функция, которая проверяет не заполнено ли все 
# игровое поле, приводящее к ничьей
def isBoardFull(board):
    # возвращает True, если все клетки на игровом заняты. 
    # В противном случае возвращает False
    for i in range(1,10):
        if isSpaceFree(board,i):
            return False
    return True


# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

print('Игра "КРЕСТИКИ-НОЛИКИ"')

while True:
    # Перезагрузка игрового поля
    theBoard = [' ']*10

    # определяем символы у компьютера и человека
    plaerLetter, computerLetter = inputPlayerLetter()

    # щпределяем кто ходит первым и выводим сообщение об этом на экран
    turn = whoGoesFirst()
    print(''+turn+' ходит первым.')

    # создадим переменную, которая будет True, пока игра не закончилась
    gameIsPlaying = True

    # запускаем игру
    while gameIsPlaying:
        # проверяем чей ход
        if turn == 'Человек':
            # ход человека
            # покажем игровое поле
            displayBoard(theBoard)
            # принимаем от человека ход
            move = getPlayerMove(theBoard)
            # делаем принятый ход
            makeMove(theBoard,plaerLetter,move)

            # проверяем не выиграл ли человек
            if isWinner(theBoard,plaerLetter):
                # если человек выиграл
                # покажем игровое поле
                displayBoard(theBoard)
                # позравим человека
                print('Поздравляю! Ты выиграл!')
                # покажем, что игра закончилась 
                # изменив переменную на False
                gameIsPlaying = False
            else:
                # человек не выиграл, 
                # проверим нет ли ничьей
                if isBoardFull(theBoard):
                    # все клетки заполнены - ничья 
                    # покажеи игровое поле
                    displayBoard(theBoard)
                    # сообщим о ничьей
                    print('Ничья!')
                    # завершаем игру прерыванием цикла
                    break
                else:
                    # нет ни победы, ни ничьей, 
                    # можно передавать ход
                    turn = 'Компьютер'
        else:
            # ход компьютера 
            # получаем ход от ИИ
            move = getComputerMove(theBoard,computerLetter)
            # делаем полученный ъод
            makeMove(theBoard,computerLetter,move)

            # проверяем не выиграл ли ИИ
            if isWinner(theBoard,computerLetter):
                # если ИИ выиграл
                # покажем игровое поле
                displayBoard(theBoard)
                # сообщим о проигрыше
                print('ИИ был сильнее! Вы проиграли!')
                # покажем, что игра закончилась 
                # изменив переменную на False
                gameIsPlaying = False
            else:
                # ИИ не выиграл, 
                # проверим нет ли ничьей
                if isBoardFull(theBoard):
                    # все клетки заполнены - ничья 
                    # покажеи игровое поле
                    displayBoard(theBoard)
                    # сообщим о ничьей
                    print('Ничья!')
                    # завершаем игру прерыванием цикла
                    break
                else:
                    # нет ни победы, ни ничьей, 
                    # можно передавать ход
                    turn = 'Человек'

    print('Сыграем еще раз? (да или нет)')
    if not input().lower().startswith('д'):
        break