# ********************************************************
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# ********************************************************
import random
# ********************************************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# ********************************************************

# функция настроек
def nastroyki():
    print('ИГРА "НАПЕРСТКИ"')
    print()
    print('Автор: Вашкеба Игорь')
    print()
    print('Версия 1.0')
    print()
    
    print('Введите сколько у игрока денег')
    dengi = input()
    while True:
        if dengi.isdigit():
            dengi = int(dengi)
            break
        else:
            print('Надо вводить только цифры')
            dengi = input()

    print('Введите размер минимальной ставки')
    minStavka = input()
    while True:
        if minStavka.isdigit():
            minStavka = int(minStavka)
            break
        else:
            print('Надо вводить только цифры')
            minStavka = input()

    return [dengi,minStavka]        

def intro():
    print('''    Вы приходите на рынок.

    На рынке вы видите человека сидящего за столом.

    Перед ним три наперска и маленький шарик.

    Заинтересовавшись, вы подходите к человеку.

    Он предлагает вам испытать свою удачу 
    и сыграть с ним на деньги''')

def proverka(dengi,minStavka):
    print('Сделайте вашу ставку')
    stavka = input()
    while True:
        if stavka.isdigit():
            # переводи строку в число
            stavka = int(stavka)
            # проверяем что ставка больше минимальной
            if stavka > minStavka:
                # проверяем, что ставка меньше количества денег у игрока
                if stavka > dengi:
                    print('Ставка не может быть больше суммы денег у игрока')
                    stavka = input()
                else:
                    break
            else:
                print('Ставка не может быть меньше минимальной')
                stavka = input()
        else:
            print('Надо вводить только цифры')
            stavka = input()
    return stavka

def sravnenie(game,igrok):
    if game == igrok:
        sovpadenie = True
    else:
        sovpadenie = False
    return sovpadenie

def intro2():
    print('''    После сделанной вами ставки
    ведущий начинает с большой скоростью перемещать
    наперстки по столу.
    
    Остановившись, он предлагает вам
    выбрать наперсток под которым,
    как вы думаете находится шарик.''')

def otvet():
    print('Введите номер наперстка:')
    nap = input()
    while True:
        if nap.isdigit():
            if (nap in '123') and (len(nap)==1):
                nap = int(nap)
                break
            else:
                print('Надо ввести только 1,2 или 3')
                nap = input()
        else:
            print('Надо вводить цифры.')
            nap = input()
    return nap

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

def autor():
    print()
    print('************************************')
    print('   .___.       Н А П Е Р С Т К И')   
    print("___('v')___    Автор: Игорь")
    print('`"-\._./-"     Верия 1.0')
    print('    ^ ^')        
    print('************************************')
    print()

# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************
autor()
many,minBig = nastroyki()
intro()

while True:
    stavkaIgroka = proverka(many,minBig)
    intro2()
    napG = random.randint(1,3)
    napI = otvet()
    if sravnenie(napG,napI):
        print('Поздравляю! Ты выиграл!')
        many = many + stavkaIgroka
    else:
        print('Увы, ты проиграл')
        many = many - stavkaIgroka

    if many > minBig:
        # зададим вопрос хочет ли человек сыграть еще
        if playAgain():
            print('Продолжаем играть. В наличии '+str(many))
        else:
            print('Хорошо. Игра закончена. В наличии '+str(many))
            autor()
            break
    else:
        print('У вас осталось денег меньше минимальной ставки.')
        print('В наличии '+str(many)+'. Игра будет завершена.')
        autor()
        break
