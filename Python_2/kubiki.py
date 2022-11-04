# Игра "21"

# ********************************************************
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# ********************************************************
import random
# ********************************************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# ********************************************************

def kubiki():
    kubiki = ['''
 ---
|   |
|   |
|   |
 ---
''','''
 ---
|   |
| * |
|   |
 ---
''','''
 ---
|*  |
|   |
|  *|
 ---
''','''
 ---
|*  |
| * |
|  *|
 ---
''','''
 ---
|* *|
|   |
|* *|
 ---
''','''
 ---
|* *|
| * |
|* *|
 ---
''','''
 ---
|* *|
|* *|
|* *|
 ---
''']
    return kubiki

def help():
    print('''       Человек кидает по два кубика некоторое количество раз,
    пытаясь набрать 21 очко в сумме. Он может остановиться 
    на любом ходе и передать ход компьютеру.
       Если он набирает больше 21 очка в сумме, то признается
    проигравшим.
       Когда ход переходит к компьютеру он также начинает
    бросать по два кубика, пыткаясь набрать количество
    очков больше, чем у человека. Как только он перебил 
    количество очков человека, игра заканчивается и 
    выигравшим признается компьютер.
       Если в попытке перебить компьютер наберет больше 
    21 очка - он проиграл.
       Если компьютер набирает количество очков равное
    человеку, то признается ничья.
    ''')

def brosok():
    k1 = random.randint(1,6)
    k2 = random.randint(1,6)
    kub = []
    kub.append(k1)
    kub.append(k2)
    return kub

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

def vHelp():
    print('Хотите прочитать правила? (да или нет).')
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
Введите "да", что бы прочитать правила и "нет" для начала игры''')

def display(kubiki,kub1,kub2,balG,balK,gamer):
    print(gamer)
    print(kubiki[kub1])
    print(kubiki[kub2])
    print()
    print('Количество очков:')
    print('Человек - '+str(balG)+'. Компьютер - '+str(balK)+'.')

def hodP():
    print('Бросаем (Б) или передаем ход?')
    while True:
        if input().lower().startswith('б'):
            return True
        else:
            return False
#        else:
#            print('введите правильный ответ.')

def proverkaBals(bG,bK):
    if bK > 21:
        return False
    elif bK > bG:
        return False
    elif bK == bG:
        return False
    else:
        return True

# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

print('Игра "Кубики. 21."')

kub = kubiki()

games = True

while games:
    if vHelp():
        help()
        s = input('Для продолжения нажмите Enter.')


    gamer = 'Человек'
    bG = 0
    bK = 0
    g = True
    gk = True

    pris = True

    while g:

        o1,o2 = brosok()
        bG = bG + o1 + o2
        display(kub,o1,o2,bG,bK,gamer)

        if bG > 21:
            print('Увы! Вы проиграли!')
            g = False
            gk = False
            pris = False
        else:    
            g = hodP()

    gamer = 'Компьютер'

    while gk:
        
        o1,o2 = brosok()
        bK = bK + o1 + o2
        display(kub,o1,o2,bG,bK,gamer)

        s = input('Для продолжения нажмите Enter.')

        gk = proverkaBals(bG,bK)

#    if pris:
    if bK > 21:
        print('Поздравляю! Вы выиграли!')
    elif bK > bG:
        print('Увы! Вы проиграли!')
    elif bK == bG:
        print('Ничья!')

    games = playAgain()    
