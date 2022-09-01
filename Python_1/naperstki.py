# импортируем модуль random
import random
# устанавливаем минимальную ставку
minBig = 10
# выдаем сумму денег
many = 1000

def autor():
    print('************************************')
    print('   .___.       Н А П Е Р С Т К И')   
    print("___('v')___    Автор: Игорь")
    print('`"-\._./-"     Верия 1.0')
    print('    ^ ^')        
    print('************************************')


def intro():
    # рассказываем об игре
    print('''Вы заходите на рынок.
Видите человека перед которым стоит стол,
на котором стоят три наперстка.
Он показывает, что под одним из них шарик.
Он предлагает вам сделать ставку 
и попробовать отгадать под каким
наперстком будет шарик.''')

def stavkaF(dengiV):
    # проверяем ставку
    print('В наличии денег: '+str(dengiV))
    print('Напишите, какую ставку вы делаете (не меньше 10)')
    # делаем ставку
    stav = input()
    stav = int(stav)
    # проверяем ставку, она должна быть не меньше минимальной
    # делаем бесконечный цикл, чтобы не пропустить ставку меньше минимальной
    while True:
        if stav < minBig:
            print('Ставка не может быть меньше '+str(minBig)+'. Введите ставку.')
            # требуем ввести ставку по новой
            stav = input()
            stav = int(stav)
        elif stav > many:
            print('У вас нет столько денег чтобы сделать ставку. В наличии '+str(many)+'.')
            # требуем ввести ставку по новой
            stav = input()
            stav = int(stav)
        else:
            # ставка нормальная, идем дальше
            break

    return stav

def intro2():
    # делаем рассказ
    print('''После того как вы сделали ставку
ведущий начинает перемещать по столу наперстки, приговаривая:
"Кручу, верчу, запутать хочу"''')
    print()
    print('Остановив движение наперстков, ведущий предлагает отгадать под которым шарик')
    print()
    print('Введите номер наперска, под которым вы считает находится шарик')

def proverka():
    nomNap = input()
    while True:
        if nomNap.isdigit():
            if len(nomNap)==1:
                if nomNap in '123':
                    nomNap = int(nomNap)
                    break
                else:
                    print('Надо ввести 1, 2 или 3')
                    nomNap = input()
            else:
                print('Надо ввести только одну цифру')
                nomNap = input()
        else:
            print('Надо ввести только цифру')
            nomNap = input()        
    return nomNap

def playAgain(dengi,minStavka):
    if dengi > minStavka:
        print('Вы хотите сыграть еще? да или нет')
        otvet = input()
        while True:
            if otvet == 'да':
                # игра продолжается
                play = True
                break
            elif otvet == 'нет':
                # игра заканчивается
                play = False
                break 
            else:
                print('Не понял ответа')
                otvet = input()
    else:
        print('У вас осталось денег менше минимальной ставки.')
        print('В наличии '+str(dengi)+'. Игра закончилась')
        play = False

    return play    

# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# рассказываем об игре
autor()

intro()
# выводим пустую строку
print()
# проверяем есть ли деньги для игры
while True:
    # проверяем ставку и возвращаем ее в переменную
    stavka = stavkaF(many)

    # выбираем где у нас будет шарик
    napS = random.randint(1,3)

    intro2()

    napV = proverka()

    # проверяем на совпадение загаданный наперсток и введенный игроком
    if napS == napV:
        # отгадали - возвращается сумма ставки * 2
        print('Поздравляю вы выиграли '+ str(stavka))
        many = many + stavka
    else:
        # не отгадали - из денег списывается ставка
        print('Увы, вы проиграли '+str(stavka))
        many = many - stavka

    if not playAgain(many,minBig):
        # игра закончилась
        print('Вы закончили игру. У вас в наличии '+str(many))
        autor()
        break