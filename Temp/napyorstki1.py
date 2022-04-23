# "Это игра наперстки"
import random,time

def displayIntro():
    print('''Он показывает маленький шарик, 
    который накрывает одним из наперстков...''')
    time.sleep(2)
    print('''После этого он начинает перемещать наперстки
    все с большей скоростью, что даже трудно отследить 
    расположение наперстка с шариком.''')
    time.sleep(2)
    print('''При этом он не престает произносить фразу
    "Кручу-верчу, запутать хочу."
    ''')

def vvodGamer():
    print('''Вы решили попытать удачу, отгадав под
    каким из наперстков находится шарик! Укажите
    номер наперска, введя одно из чисел "1", "2" или "3".''')
    vybor = input()
    while vybor != '1' and vybor != '2' and vybor != '3':
        print('Введите "1","2" или "3"!') 
        vybor = input()
    return vybor

def playGames(myVybor):
    naperstok = random.randint(1,3)
    if int(myVybor) == int(naperstok):
        # игрок выиграл
        print('... вы выиграли!')
    else:
        # игрок проиграл
        print('... вы проиграли!')
        

print('Как тебя зовут?')
myName = input()
print(myName+''', вы идете по рынку и видите
    человека, сидящего за столом. На столе перед ним
    находятся три наперстка.''')
doneGames = 'да'
while doneGames == 'да' or doneGames == 'д':
    displayIntro()
    otvetGamer = vvodGamer()
    playGames(otvetGamer)
    print('Вы хотите сыграть еще раз?')
    doneGames = input()



    