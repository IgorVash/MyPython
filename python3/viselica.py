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
    words = 'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()    
    return words

def vyborSlova(spis):
    indSl = random.randint(0,len(spis)-1)
    slovo = spis[indSl]
    return slovo

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

def displayBoard(nasyVis,errorBuk,yesBuk,sicretSl):
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
sicretSlovo = vyborSlova(wordsS)

strokaErrorB = ''
strokaYesB = ''

while True:
    displayBoard(vis,strokaErrorB,strokaYesB,sicretSlovo)
    vvedenayaB = proverka(strokaErrorB+strokaYesB)