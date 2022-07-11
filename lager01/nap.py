# *****************************************
# ПОДКЛЮЧАЕМЫЕ МОДУЛИ
# *****************************************
import random
# *****************************************
# СОБСТВЕННЫЕ ФУНКЦИИ
# *****************************************
def nastroyki():
    while True:
        print('Введите сколько денег у игрока:')
        many = input()
        if many.isdigit():
            many = int(many)
            break
        else:
            print('Надо вводить только цифры.')

    while True:
        print('Введите размер минимальной ставки:')
        minS = input()
        if minS.isdigit():
            minS = int(minS)
            if minS > many:
                print('Минимальная ставка не может быть больше денег в наличии')
            else:
                break
        else:
            print('Надо вводить только цифры.')

    return [many,minS]

def intro():
    print('''
            В воскресенье мы всей семьей решили посетить
    местный рынок. Когда мы туда приехали, на входе я увидел
    человека сидящего за столом. Перед ним стояли три пласти-
    ковых стаканчика. Он демонстрировал подходящим людям, что
    под одним из них прячется небольшой шарик и предлагал от-
    гадать где он будет, после того как он некоторое время 
    будет перемещать стаканчики по столу.
    ''')

def stavka(manyNal,minSt):
    while True:
        print('Введите ставку:')
        stavka = input()
        if stavka.isdigit():
            stavka = int(stavka)
            if stavka < minSt:
                print('Ставка не может быть меньше минимальной')
            elif stavka > manyNal:
                print('Ставка не может быть больше, чем денег в наличии.')
            else:
                return stavka
        else:
            print('Надо вводить только цифры')


# *****************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# *****************************************
manyIgroka,minStavka = nastroyki()
#print('У игрока '+str(manyIgroka)+' рублей')
#print('минимальная ставка '+str(minStavka)+' рублей')
intro()
while True:
    stavkaIgroka = stavka(manyIgroka,minStavka)
    print('Вы поставили '+str(stavkaIgroka)+' рублей.')