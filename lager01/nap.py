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
            Вы решили подойти ближе.
            После небольшого раздумья, вы решили
    попытать счатья и сыграть.
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

def intro2():
    print('''
        После того как вы сделали свою ставку,
    ведущий показал вам шарик и накрыл его стаканчиком.
        После этого он стал перемещать стаканчики по
    столу, приговаривая:
        "Кручу-верчу, запутать хочу!"
        Он остановился и посмотрел на вас.
    ''')

def vybor():
    while True:
        print('Выбери наперсток под которым, как ты думаешь, находится мячик:')
        otvet = input()
        if otvet.isdigit():
            otvet = int(otvet)
            if otvet in (1,2,3):
                return otvet
            else:
                print('Вы должны ввести 1, 2 или 3')
        else:
            print('Вводите только числа')

def sravnenie(per1,per2):
    if per1 == per2:
        return True
    else:
        return False

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

    napG = random.randint(1,3)

    intro2()

    napI = vybor()

    if sravnenie(napG,napI):
        print('Поздравляю, ты выиграл!')
        manyIgroka = manyIgroka + stavkaIgroka # manyIgroka =+ stavkaIgroka
    else:
        print('Увы, ты проиграл!')
        manyIgroka = manyIgroka - stavkaIgroka

    if manyIgroka < minStavka:
        print('У тебя осталось '+str(manyIgroka)+''' рублей.')
        Это меньше чем минимальная ставка.
        Ты не можешь продолжать играть. Игра будет завершена''')
        break
    else:
        if not playOwer():
            print('''Хорошо, прекращаем игру.
            У вас осталось '''+str(manyIgroka)+' рублей')
            break
        else:
            print('У вас стало '+str(manyIgroka)+' рублей')