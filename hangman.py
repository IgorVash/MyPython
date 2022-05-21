import random
HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  0   |
      |
      |
     ===''','''
  +---+
  0   |
  |   |
      |
     ===''','''
  +---+
  0   |
 /|   |
      |
     ===''','''
  +---+
  0   |
 /|\  |
      |
     ===''','''
  +---+
  0   |
 /|\  |
 /    |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']
words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()

def getRandomWord(wordList):
    # Эта функция возвращает случайную строку из переданного списка.
    wordIndex = random.randint(0, len(wordList)-1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Ошибочные буквы:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): # заменяет пропуски отгаданными буквами
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks[i+1:]

    for letter in blanks: # показывает секретное слово с пробелами между буквами
        print(letter, end=' ' )
    print()

def getGuess(alreadyGuessed):
    # возвращает букву, введенную игроком. Эта функция проверяет, что игрок вве только одну букву и ничего больше
    while True:
        print('Введите букву.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Пожалуйста, введите одну букву.')
        elif guess in alreadyGuessed:
            print('Вы уже называли эту букву. Назовите другую.')
        elif guess not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ')
        else:
            return guess

def playAgain():
    # Эта функция возвращает True, если игрок хочет сыграть заново, в противном False
    print('Хотите сыграть еще? (да или нет).')
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            # ответ да, запускаем игру по новой
            return True
        elif (otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            # игрок отказался от игры, завершаем
            return False
        else:
            print('''Я вас не понял! 
Введите ответ еще раз.
Введите "да" для продолжения и "нет" для завершения игры''')

def vyborS():
    print('Выберите уровень сложности.')
    print('Введите "Л" для легкого уровня,')
    print('"С" для среднего и')
    print('"Т" для тяжелого.')

    while True:
        us = input().upper()
        print(us)
        if len(us) != 1:
            print('Введите только одну букву.')
        elif us not in 'ЛСТ':
            print('Введите "Л" для легкого уровня,')
            print('"С" для среднего и')
            print('"Т" для тяжелого.')
        else:
            print('123')
            print(us)
            return us
#            break


def delV(urovenS):
    urovenS = vyborS()
    if urovenS == 'С':
        del HANGMAN_PICS[10]
        del HANGMAN_PICS[9]
    elif urovenS == 'Т':
        del HANGMAN_PICS[10]
        del HANGMAN_PICS[9]
        del HANGMAN_PICS[8]
        del HANGMAN_PICS[7]

uroven = vyborS()
delV(uroven)

errorB = ''
yesB = ''
gameOver = False
sicretS = getRandomWord(words)

while True:
    displayBoard(errorB,yesB,sicretS)

    bukva = getGuess(errorB+yesB)

    if bukva in sicretS:
        yesB = yesB + bukva
 
        # Проверяет, выиграл ли игрок
        ssYes = True
        for i in range(len(sicretS)):
            if sicretS[i] not in yesB:
                ssYes = False
                break
        if ssYes:
            print('ДА! Секретное слово - "'+sicretS+'"! Вы угадали!')
            gameOver = True
    else:
        errorB = errorB + bukva
        if len(errorB) == len(HANGMAN_PICS) - 1:
            displayBoard(errorB,yesB,sicretS)
            print('Вы исчерпали все попытки!\nНеугадано букв:'+str(len(errorB))+'\nугадано букв:'+str(len(yesB))+'.\nБыло загадано слово "'+sicretS+'".')
            gameOver = True

    # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if gameOver:
        if playAgain():
            delV(vyborS())

            errorB = ''
            yesB = ''
            gameOver = False
            sicretS = getRandomWord(words)
        else:
            break
