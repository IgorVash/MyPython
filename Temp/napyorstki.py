import random,time

def displayIntro():
    print('''Вы неспеша идете по местному рынку.
Вдруг вы видите человека, который предлагает сыграть прохожим в игру.
Перед ним стоит стол, на нем три наперстка и маленький шарик.
Он демонстрирует, что в наперстках ничего нет.
Потом накрывает одним наперстком шарик и...''')
    time.sleep(2)
    print(''' начинает быстро перемещать
наперстки по столу. При этом приговаривая:
"Кручу, верчу, запутать хочу."''')
    time.sleep(2)
    print('''Он останавливает движение наперстков
и предлагает отгадать, под каким наперстком
находится шарик.''')


def chooseAThimble():
    thimble = ''
    while thimble != '1' and thimble != '2' and thimble != '3':
        print('Вы некоторое время раздумывете...')
        time.sleep(2)
        print('и называете номер наперстка. (введите 1, 2 или 3)')
        thimble = input()

    return thimble


def checkAThimble(choosenAThimble):
    print('Ведущий поднимает указанный вами наперсток и...')
    time.sleep(4)

    ballUnderThimble = random.randint(1, 3)

    if choosenAThimble == str(ballUnderThimble):
        print('... под ним оказывается шарик! Вы выиграли!')
    else:
        print('... под наперстком пусто. Вы проиграли.')


playAgain = 'да'
while playAgain == 'да' or playAgain == 'д':
    displayIntro()

    thimbleNumber = chooseAThimble()

    checkAThimble(thimbleNumber)

    print('Попытаете удачу еще раз? (да или нет)')
    playAgain = input()
