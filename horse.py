# ********************************************************
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# ********************************************************
import random,os
# ********************************************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# ********************************************************

def zastavka():
    print()
    print('******************************************************************')
    print('       /\/\    $$$$$   $$   $$   $$$$$   $$   $$  $$   $$  $$   $$')
    print('      /    \  $$   $$  $$  $$   $$   $$  $$   $$  $$  $$   $$  $$$')
    print('    ~/(^  ^)  $$       $$$$     $$$$$$$   $$$$$$  $$$$     $$ $ $$')   
    print('   ~/  )  (   $$   $$  $$  $$   $$   $$       $$  $$  $$   $$$  $$')
    print('  ~/   (  )    $$$$$   $$   $$  $$   $$       $$  $$   $$  $$   $$')
    print(' ~/     ~~    ----------------------------------------------------')
    print('~/       |           ВЕРСИЯ 1.0        АВТОР: ИГОРЬ ВАШКЕБА')
    print('******************************************************************')
    print()

def nastroyki():

    while True:
        many = input('       Введите сколько денег будет у игрока:   ')
        if not many.isdigit():
            # игрок ввел не только цифры
            print('       Вы должны вводить только цифры.')
        else:
            many = int(many)
            break

    while True:        
        minSt = input('       Введите размер минимальной ставки:   ')
        if not minSt.isdigit():
            print('       Вы должны вводить только цифры.')
        else:
            minSt = int(minSt)
            break

    return [many,minSt]

def intro1():
    print('''
       У вас сегодня хорошее настроение и  вы  решили
    посетить местный ипподром, что бы  испытать  свою
    удачу, сделав ставку на одну из четырех лошадей в 
    забеге.''')

def intro2():
    print('''
       Изучив лошадей, участвующих в забеге, вы подош-
    ли к кассе, чтобы сделать ставку.''')

def stavka(many,minSt):
    while True:
        print('       Введите номер лошади, от 1 до 4, на которую хотите поставить:')
        horse = input()
        if not horse.isdigit():
            print('       Надо ввести цифру.')
        elif len(horse) != 1:
            print('       Надо вводить цифру от 1 до 4')
        elif horse not in '1234':
            print('       Надо вводить цифру от 1 до 4')
        else:
            horse = int(horse)
            break

    while True:
        print('       Введите сумму, которую хотите поставить на выбранную лошадь:')
        stavka = input()
        if not stavka.isdigit():
            print('       Надо вводить только цифры.')
        else:
            stavka = int(stavka)
            if stavka < minSt:
                print('       Ставка не может быть меньше минимальной.')
                print('       Минимальная ставка '+str(minSt)+'.')
            elif stavka > many:
                print('       Ставка не может быть больше суммы денег в наличии у игрока.')
                print('       У игрока в наличии '+str(many)+'.')
            else:
                stavka = int(stavka)
                break

    return [horse,stavka]            

def playAgain():
    # Эта функция возвращает True, если игрок хочет сыграть заново, в противном False
    print('       Хотите сыграть еще? (да или нет).')
    while True:
        otvet = input().lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            # ответ да, запускаем игру по новой
            return True
        elif (otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            # игрок отказался от игры, завершаем
            return False
        else:
            print('''
       Я вас не понял! 
       Введите ответ еще раз.
       Введите "да" для продолжения и "нет" для завершения игры.''')


def startGame():
    h = [0,0,0,0]
    l = [90,90,90,90]
    victory = 0
    while True:
        for i in range(1,5):
            if l[i-1]>0:
                print(str(i)+' '+'_'*h[i-1]+'*'+'_'*l[i-1])
                hp = random.randint(1,3)
                h[i-1] = h[i-1] + hp
                l[i-1] = l[i-1] - hp
            else:
                if victory == 0:
                    victory = i
                print(str(i)+' '+'_'*90+'*')

        print()
        print()
        if (not h[0]<90) and (not h[1]<90) and (not h[2]<90) and (not h[3]<90):
            os.system('cls' if os.name == 'nt' else 'clear')    
            for i in range(1,5):
                print(str(i)+' '+'_'*90+'*')
            break
        else:
            s = input('Нажмите "Enter" для продолжения')
            os.system('cls' if os.name == 'nt' else 'clear')

    return victory


# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

zastavka()
intro1()
myMany, minStavka = nastroyki()
while True:
    intro2()

    myHorse, myStavka = stavka(myMany,minStavka)

    print('''
       Прозвучал гонг и скачка началась!
       
       ''')

    vict = startGame()

    if vict == myHorse:
        print('''
       Вы выиграли '''+str(myStavka))
        myMany = myMany + myStavka
    else:
        print('''
       Первой пришла лошадь под номером '''+str(vict)+''',
    вы ставили на лошадь под номером '''+str(myHorse)+'''. 
       Вы проиграли '''+str(myStavka))
        myMany = myMany - myStavka

    if myMany < minStavka:
        print('''
       У вас в наличии денег меньше размера минимальной ставки.
       Вы больше не можете делать ставки и поэтому покидаете
    ипподром.
       у вас в наличии остается '''+str(myMany)+'.')
        break
    else:
        if not playAgain():
            print('''
       Отлично!
       Вы покидаете ипподром и у вас в наличии '''+str(myMany)+'.')
            break
