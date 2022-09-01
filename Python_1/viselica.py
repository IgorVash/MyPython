# ********************************************************
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# ********************************************************
import random
# ********************************************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# ********************************************************
def genVis():
    # функция которая генерирует изображение виселиц
    HANGMAN_PIC = ['''
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
     ===''','''
  +---+
 [0   |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
 /|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
[/|\  |
 / \  |
     ===''','''
  +---+
 [0]  |
[/|\] |
 / \  |
     ===''']
    return HANGMAN_PIC

def genWorldList():
    # функция которая генерирует список слов для отгадывания
    words = {'цвета':'красный оранжевый желтый зеленый голубой синий фиолетовый белый черный коричневый'.split(),
    'фигуры':'треугольник квадрат прямоугольник круг овал пятиугольник трапеция ромб шестиугольник звезда'.split(),
    'фрукты':'апельсин ананас абрикос банан виноград груша грейпфрукт яблоко лимон лайм мандарин персик манго нектарин'.split(),
    'животные':'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()}
    return words

def vyborUS():
    while True:
        print('''Выберите уровень сложности:
Введите "Л" или "L" для легкого уровня,
"Н" или "N" для нормального и
"Х" или "H" для тяжелого уровня.''')
        urSl = input()
        urSl = urSl.upper()
        if len(urSl) != 1:
            print('Введите только одну букву')
        elif urSl not in 'ЛНХLNH':
            print('Введите только "Л", "Н", "Х", "L", "N" или "H"')
        elif (urSl == 'Л') or (urSl == 'L'):
            return 'Light'
        elif (urSl == 'Н') or (urSl == 'N'):
            return 'Norma'
        elif (urSl == 'Х') or (urSl == 'H'):
            return 'Hard'


def proverkaVvoda(strBuk):
    # возвращает букву, введенную игроком. Эта функция проверяет, 
    # что игрок ввел только одну русскую букву и ничего больше
    # запускаем бесконечный цикл
    while True:
        # говорим игроку, что бы он ввел букву и принимаем то что он ввел
        print('Введите букву.')
        frasa = input()
        # переводим введенное игроком в нижний регистр
        frasa = frasa.lower()
        # проверяем что введена одна буква
        if len(frasa) != 1:
            print('Пожалуйста, введите одну букву.')
        # проверяем, что буква не была введена ранее
        elif frasa in strBuk:
            print('Вы уже называли эту букву. Назовите другую.')
        # проверяем, что введена русская буква
        elif frasa not in 'абвгдежзийклмнопрстуфхцчшщъыьэюя':
            print('Пожалуйста, введите БУКВУ')
        else:
            # прерываем бесконечный цикл и возвращаем введенную букву
            return frasa

def displayBoard(errorStr,yesStr,sicretSlovo,vis,usDysp,sicretKey):
    # в функцию должны передаваться несколько переменных
    # строка с ошибочными буквами
    # строка с правильными буквами
    # слово, которое отгадываем
    # список с нашими виселицами
    # выводим ключ словаря
    if usDysp == 'Hard':
        strKey = ''
    else:
        strKey = 'Категория слова: '+sicretKey
    print(strKey)
    print(vis[len(errorStr)])
    # выводим виселицу с учетом количества ошибочных букв
    print()
    # пустая строка
    print('Ошибочные буквы: '+errorStr)
    # список ошибочных букв
    blanks = '_'*len(sicretSlovo)
    for i in range(len(sicretSlovo)): # заменяет пропуски отгаданными буквами
        if sicretSlovo[i] in yesStr:
            blanks = blanks[:i] + sicretSlovo[i] + blanks[i+1:]
    for letter in blanks: # показывает секретное слово с пробелами между буквами
        print(letter, end=' ' )
    print()
    # слово с отгаданными буквами

def playAgain():
    # Эта функция возвращает True, если игрок хочет сыграть заново, в противном False
    print('Хотите сыграть еще? (да или нет).')
    while True:
        otvet = input()
        otvet = otvet.lower()
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

def autor():
    print()
    print('************************************')
    print('   .___.       В И С Е Л И Ц А')   
    print("___('v')___    Автор: Игорь")
    print('`"-\._./-"     Верия 1.0')
    print('    ^ ^')        
    print('************************************')
    print()

def getRandomWorld(spS,usV):
    if usV == 'Light':
        for i in range(len(list(spS.keys()))):
            print('Введите '+str(i)+' для '+list(spS.keys())[i])
        vybK = input()
        vybK = int(vybK)
        wordKey = list(spS.keys())[vybK]
    else:
        wordKey = random.choice(list(spS.keys()))
    
    wordIndex = random.randint(0, len(spS[wordKey])-1)
    return [spS[wordKey][wordIndex],wordKey]

def delVis(usD,hang):
    if usD == 'Norma':
        del hang[10]
        del hang[9]
    elif usD == 'Hard':
        del hang[10]
        del hang[9]
        del hang[8]
        del hang[7]


# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

numberProhod = True

while True:
    if numberProhod:
        # помещаем в переменную viselica наши сгенерированные виселицы
        viselica = genVis()
        # помещаем в переменную wordList наши слова для отгадывания 
        wordList = genWorldList()
        uroven = vyborUS()
        # выбираем слово для отгадывания случайным образом
        sl,keySl = getRandomWorld(wordList,uroven)
        # удаляем необходимое количество виселец в зависимости от уровня сложности
        delVis(uroven,viselica)
        autor()
        # создаем пустые строки с правильными и ошибочными буквами
        errorB = ''
        yesB = ''
        # создаем переменную в которую помещаю Истину, если игра окончена и Ложь если игра продолжается
        gameOver = False
        numberProhod = False
        
    # выводим на экран игровое поле
    displayBoard(errorB,yesB,sl,viselica,uroven,keySl)
    # требуем ввести букву для отгадывания
    bukva = proverkaVvoda(errorB+yesB)
    # проверяем есть ли введенная буква в слове для отгадывания
    if bukva in sl:
        yesB = yesB + bukva
 
        # Проверяет, выиграл ли игрок
        ssYes = True
        for i in range(len(sl)):
            if sl[i] not in yesB:
                ssYes = False
                break
        if ssYes:
            print('ДА! Секретное слово - "'+sl+'"! Вы угадали!')
            gameOver = True
    else:
        errorB = errorB + bukva
        if len(errorB) == len(viselica) - 1:
            displayBoard(errorB,yesB,sl,viselica,uroven,keySl)
            print('Вы исчерпали все попытки!\nНеугадано букв:'+str(len(errorB))+'\nугадано букв:'+str(len(yesB))+'.\nБыло загадано слово "'+sl+'".')
            gameOver = True

    # Запрашивает, хочет ли игрок сыграть заново (только если игра завершена).
    if gameOver:
        if playAgain():
            numberProhod = True
        else:
            autor()
            break
