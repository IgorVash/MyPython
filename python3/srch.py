import random
# подключили модуль random
print('Привет, как тебя зовут?')
myName = input()
# Поздоровались, спросили имя, ответ записали в переменную myName
s = random.randint(1,20)
print('Я загадала число от 1 до 20.')
# программа загадала (сгененерировала) число от 1 до 20 и рассказала об этом игроку
for i in range(3):
    # даем игроку 3 попытки отгадать число
    print('Введи число от 1 до 20')
    y = input()
    # программа просит ввести число и записывает введенное в переменную y
    while True:
        if y.isdigit():
            break
        else:
            print('Введи число.')
            y = input()
    y = int(y)
    # переводи строку в число
    if s > y:
        print('Твое число менше загаданного')
    if s < y:
        print('Твое число больше загаданного')
    if s == y:
        break
if s == y:
    print('Поздравляю! Ты выиграл.')
if s != y:
    print('Увы! Загаданное число '+str(s))