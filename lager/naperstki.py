# импортируем модуль random
import random
# устанавливаем минимальную ставку
minBig = 10
# выдаем сумму денег
many = 1000
# рассказываем об игре
print('''Вы заходите на рынок.
Видите человека перед которым стоит стол,
на котором стоят три наперстка.
Он показывает, что под одним из них шарик.
Он предлагает вам сделать ставку 
и попробовать отгадать под каким
наперстком будет шарик.''')
print()
while many > minBig:
    print('Напишите, какую ставку вы делаете (не меньше 10)')
    # делаем ставку
    stavka = input()
    stavka = int(stavka)
    # проверяем ставку, она должна быть не меньше минимальной
    # делаем бесконечный цикл, чтобы не пропустить ставку меньше минимальной
    while True:
        if stavka < minBig:
            print('Ставка не может быть меньше '+str(minBig)+'. Введите ставку.')
            # требуем ввести ставку по новой
            stavka = input()
            stavka = int(stavka)
        elif stavka > many:
            print('У вас нет столько денег чтобы сделать ставку. В наличии '+str(many)+'.')
            # требуем ввести ставку по новой
            stavka = input()
            stavka = int(stavka)
        else:
            # ставка нормальная, идем дальше
            break
    # выбираем где у нас будет шарик
    napS = random.randint(1,3)
    # делаем рассказ
    print('''После того как вы сделали ставку
    ведущий начинает перемещать по столу наперстки, приговаривая:
    "Кручу, верчу, запутать хочу"''')
    print()
    print('Остановив движение наперстков, ведущий предлагает отгадать под которым шарик')
    print()
    print('Введите номер наперска, под которым вы считает находится шарик')
    napV = input()
    napV = int(napV)
    # проверяем на совпадение загаданный наперсток и введенный игроком
    if napS == napV:
        # отгадали - возвращается сумма ставки * 2
        print('Поздравляю вы выиграли '+ str(stavka))
        many = many + stavka
    else:
        # не отгадали - из денег списывается ставка
        print('Увы, вы проиграли '+str(stavka))
        many = many - stavka
print('У вас закончились деньги, чтобы делать ставку. В наличии '+str(many))