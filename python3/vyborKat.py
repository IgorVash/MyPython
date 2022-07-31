import random

def genSlov():
    words = {'цвета':'красный желтый зеленый оранжевый голубой синий фиолетовый белый черный коричневый'.split(),
    'фигуры':'круг квадрат треугольник ромб прямоугольник звезда шестиугольник'.split(),
    'фрукты':'апельсин ананас банан барбарис дыня слива яблоко груша'.split(),
    'животные':'аист акула бабуин баран барсук бобр бык верблюд волк воробей ворон выдра голубь гусь жаба зебра змея индюк кит кобра коза козел койот корова кошка кролик крыса курица лама ласка лебедь лев лиса лосось лось лягушка медведь моллюск моль мул муравей мышь норка носорог обезьяна овца окунь олень орел осел панда паук питон попугай пума семга скунс собака сова тигр тритон тюлень утка форель хорек черепаха ястреб ящерица'.split()}    
    return words

def vyborSlova(spis,uS):
    if uS == 'Л':
        for i in range(len(list(spis.keys()))):
            print('Для выбора категории '+list(spis.keys())[i]+' введите '+str(i))
        
        while True:
            katSlov = input()
            if not katSlov.isdigit():
                print('Введите только цифры.')
            else:
                katSlov = int(katSlov)
                if katSlov > len(list(spis.keys())):
                    print('Вы ввели неверное число.')
                else:
                    break

        kategoriya = list(spis.keys())[katSlov]
    else:
        kategoriya = random.choice(list(spis.keys()))

    return kategoriya



slovar = genSlov()
kat = vyborSlova(slovar,'Л')
print(kat)
kat = vyborSlova(slovar,'С')
print(kat)
