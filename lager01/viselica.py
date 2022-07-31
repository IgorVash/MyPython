# ********************************************************
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# ********************************************************
import random

# ********************************************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# ********************************************************

def genVis():
    HANGMAN_PICT = ['''
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
    
    return HANGMAN_PICT

def uroven():
    while True:
        print('Выберите уровень сложности.')
        print('Введите "Л" для легкого уровня,')
        print('"С" для среднего уровня и')
        print('"Т" для тяжелого уровня.')
        otvet = input()
        otvet = otvet.upper()
        if len(otvet) != 1:
            print('Ты должен вводить одну букву.')
        elif otvet not in 'ЛСТ':
            print('Ты должен ввести Л, С или Т.')
        else:
            return otvet

def delVis(visD,uS):
    if uS == 'Т':
        del visD[10]
        del visD[9]
        del visD[8]
        del visD[7]
    elif uS == 'С':
        del visD[10]
        del visD[9]

def genSlova():
    words = {'животные':'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split(),
    'фигуры':'круг квадрат прямоугольник пятиугольник звезда трапеция ромб'.split(),
    'цвета':'красный оранжевый желтый зеленый голубой синий фиолетовый коричневый черный белый'.split(),
    'фрукты':'арбуз ананас банан виноград груша ежевика яблоко'.split()}    
    return words

def proverkaVvoda(strokaBukv):
    while True:
        print('Введите букву:')
        bukva = input()
        bukva = bukva.lower()
        if len(bukva) != 1:
            print('Ты должен вводить одну букву.')
        elif bukva not in 'йцукенгшщзхъфывапролджэячсмитьбю':
            print('Ты должен вводить только русские буквы.')
        elif bukva in strokaBukv:
            print('Ты уже называл эту букву')
        else:
            return bukva

def displayBoard(vis,errorBuk,yesBuk,sicretSlovo,keySlov,uSl):
    if uSl != 'Т':
        print('Категория слова: '+keySlov)
    print(vis[len(errorBuk)])
    print()
    print('Ошибочные буквы: '+errorBuk)
    print()
    shablon = '_'*len(sicretSlovo)
    for i in range(len(sicretSlovo)):
        if sicretSlovo[i] in yesBuk:
            shablon = shablon[:i]+sicretSlovo[i]+shablon[i+1:]
    
    for s in shablon:
        print(s,end=' ')
    print()

def playOwer():
    # переделать функцию, что бы она кроме "да" еще принимала "Да","д","Д","Yes","yes","Y","y"
    while True:
        print('Ты хочешь попытать счастья еще раз?')
        otv = input()
        otv = otv.lower()
        # Проверить что человек ввел "да", функция возвращает True
        if (otv == 'да') or (otv == 'д') or (otv == 'yes') or (otv == 'y'):
            return True
        # иначе проверить что человек ввел "нет", функция возвращает False
        # проверить "Нет", "н", "No", "n", "no", "N"
        elif (otv == 'нет') or (otv == 'н'):
            return False
        # иначе сообщить ему, что не поняли ответа
        else:
            print('Не понял вашего ответа.')

def vyborSlova(slovar,urovenSlog):
    # Эта функция возвращает случайную строку из переданного списка.
    if urovenSlog == 'Л':
        for i in range(len(list(slovar.keys()))):    
            print('Введите '+str(i)+' для '+list(slovar.keys())[i])
        vybK = input()
        vybK = int(vybK)
        wordKey = list(slovar.keys())[vybK]
    else:
        wordKey = random.choice(list(slovar.keys()))

    wordIndex = random.randint(0, len(slovar[wordKey])-1)
    return [slovar[wordKey][wordIndex],wordKey]


# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

konecGame = True

while True:
    if konecGame:
        errorBukvy = ''
        yesBukvy = ''
        viselicy = genVis()
        urovenSl = uroven()
        delVis(viselicy,urovenSl)
        spisokSlov = genSlova()
        slovo,keySl = vyborSlova(spisokSlov,urovenSl)
        konecGame = False
    
    displayBoard(viselicy,errorBukvy,yesBukvy,slovo,keySl,urovenSl)

    vBukva = proverkaVvoda(errorBukvy+yesBukvy)

    if vBukva in slovo:
        yesBukvy = yesBukvy + vBukva  # yesBukvy += vBukva

        konecGame = True
        for i in range(len(slovo)):
            if slovo[i] not in yesBukvy:
                konecGame = False
                break
        if konecGame:
            print('ПОЗДРАВЛЯЮ !!! Ты отгадал слово. Загаданное слово: '+slovo)    
    else:
        errorBukvy = errorBukvy + vBukva

        if len(errorBukvy) == len(viselicy)-1:
            print('''Увы, ты проиграл!
            Отгадано букв: '''+str(len(yesBukvy))+''',
            ошибочных букв: '''+str(len(errorBukvy))+''',
            было загадано слово: '''+slovo+'.')
            displayBoard(viselicy,errorBukvy,yesBukvy,slovo,keySl,urovenSl)
            konecGame = True

    if konecGame:
        if not playOwer():
            break