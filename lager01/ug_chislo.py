# ИМПОРТ ПОДКЛЮЧАЕМЫХ МОДУЛЕЙ
import random
# СОЗДАНИЕ СВОИХ ФУНКЦИЙ
def us():
    while True:
        print('Выберите уровень сложности.')
        print('Введите 1 - для легкого, 2 - для среднего, 3 - для сложного.')
        f = input()
        f = int(f)
        if (f == 1) or (f == 2) or (f ==3):
            return f
        else:
            print('Вы должны вводить только 1, 2 или 3.')    

# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ

u = us()
if u == 1:
    a = random.randint(1,10)
    print('Загадано число от 1 до 10')
    k = 3
elif u == 2:
    a = random.randint(1,50)
    print('Загадано число от 1 до 50')
    k = 5
elif u == 3:
    a = random.randint(1,100)
    print('Загадано число от 1 до 100')
    k = 7

gameOwer = True

for i in range(k):
    print('введите число')
    b = input()
    b = int(b)
    if a < b:
        print('Загаданое число меньше.')
    elif a > b:
        print('Загаданое число больше.')
    elif a == b:
        print('Поздравляю, ты угадал')
        gameOwer = False
        break

if gameOwer:
    print('УВЫ! Загаданное число '+str(a))