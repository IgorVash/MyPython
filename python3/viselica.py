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
     ===''']
    
    return HANGMAN_PICT

def genSlov():
    words = {'цвета':'красный желтый зеленый оранжевый голубой синий фиолетовый белый черный коричневый'.split(),
    'фигуры':'круг квадрат треугольник ромб прямоугольник звезда шестиугольник'.split(),
    'фрукты':'апельсин ананас банан барбарис дыня слива яблоко груша'.split(),
    'животные':'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()}    
    return words

def vyborSlova(spis,uS):
    if uS == 'Л':
        for i in range(len(list(spis.keys()))):
            print('Для выбора категории '+list(spis.keys())[i]+' введите '+str(i))
        
        while True:
            katSlov = input()
            if not katSlov.isdigit():
                print('Введите только цифры.')
            else:
                katSlov = int(katSlov)
                if katSlov > len(list(spis.keys())):
                    print('Вы ввели неверное число.')
                else:
                    break

        kategoriya = list(spis.keys())[katSlov]
    else:
        kategoriya = random.choice(list(spis.keys()))

    indexSlova = random.randint(0,len(spis[kategoriya])-1)

    return [spis[kategoriya][indexSlova],kategoriya]

def vyborUS():
    while True:
        print('Выберите уровень сложности.')
        print('Введите "Л" для легкого уровня.')
        print('Введите "С" для среднего уровня.')
        print('Введите "Т" для тяжелого уровня.')
        uroven = input()
        uroven = uroven.upper()
        if len(uroven) != 1:
            print('Надо вводить только один символ.')
        elif uroven not in 'ЛСТ':
            print('Вы ввели неверную букву.')
        else:
            return uroven

def proverka(strbukv):
    while True:
        print('Введите букву')
        buk = input()
        buk = buk.lower()
        if len(buk) != 1:
            print('Надо ввести только одну букву')
        elif buk not in 'абвгдежзийклмнопрстуфхцчшщьыъэюя':
            print('Надо вводить только русские буквы.')
        elif buk in strbukv:
            print('Вы уже называли эту букву.')
        else:
            return buk

def displayBoard(nasyVis,errorBuk,yesBuk,sicretSl,urS,kS):
    if urS in 'ЛС':
        print(kS)
    print(nasyVis[len(errorBuk)])
    print()
    print('Ошибочные буквы: '+errorBuk)
    print()

    shablon = '_'*len(sicretSl)

    for i in range(len(sicretSl)):
        if sicretSl[i] in yesBuk:
            shablon = shablon[:i]+sicretSl[i]+shablon[i+1:]
    
    for s in shablon:
        print(s,end=' ')
    print()    

def playAgain():
    # создаем бесконечный цикл
    while True:
        # задаем вопрос и получаем ответ
        print('Хотите продолжить играть? Да или нет.')
        otv = input()
        otv = otv.lower()
        # проверяем ответ на совпадение со следущими фразами
        # "да", "Да", "ДА", "д", "y", "yes", "Yes", "YES"
        # если есть совпадение то переменной присваиваем значение True
        # и прерываем цикл командой return
        if (otv == 'да') or (otv == 'д') or (otv == 'y') or (otv == 'yes'):
            return True
        # проверяем ответ на совпадение со следущими фразами
        # "нет", "Нет", "НЕТ", "н", "n", "no", "No"
        # если есть совпадение то переменной присваиваем значение False
        # и прерываем цикл командой return
        elif (otv == 'нет') or (otv == 'н') or (otv == 'n') or (otv == 'no'):
            return False
        #  если совпадений с первыми двумя случаями нет
        #  говорим пользователю, что не поняли его ответа
        else:
            print('Я не понял ответ.')


# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

vis = genVis()
wordsS = genSlov()

strokaErrorB = ''
strokaYesB = ''
gameOver = False

urovenSl = vyborUS()
sicretSlovo,katSl = vyborSlova(wordsS,urovenSl)



while True:
    displayBoard(vis,strokaErrorB,strokaYesB,sicretSlovo,urovenSl,katSl)
    vvedenayaB = proverka(strokaErrorB+strokaYesB)

    if vvedenayaB in sicretSlovo:
        strokaYesB = strokaYesB + vvedenayaB

        konecGame = True
        for i in range(len(sicretSlovo)):
            if sicretSlovo[i] not in strokaYesB:
                konecGame = False
                break
        if konecGame:
            print('ДА! Секретное слово - "'+sicretSlovo+'"! Вы угадали!')
            gameOver = True
    else:
        strokaErrorB = strokaErrorB + vvedenayaB

        if len(strokaErrorB)==len(vis)-1:
            displayBoard(vis,strokaErrorB,strokaYesB,sicretSlovo,urovenSl,katSl)
            print('''            Вы исчерпали все попытки!
            Названо ошибочных букв: '''+str(len(strokaErrorB))+'''
            угадано букв: '''+str(len(strokaYesB))+'''
            было загадано слово: '''+sicretSlovo+'.')
            gameOver = True

    if gameOver:
        if playAgain():
            urovenSl = vyborUS()
            sicretSlovo,katSl = vyborSlova(wordsS,urovenSl)

            strokaErrorB = ''
            strokaYesB = ''
            gameOver = False
        else:
            break
