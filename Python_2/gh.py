# Игра "КРЕСТИКИ-НОЛИКИ"

# ********************************************************
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# ********************************************************
import random
# ********************************************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# ********************************************************

KOL_CIFR = 3
KOL_POP = 10

def generatorCh():
    numbers = list(range(10))
    random.shuffle(numbers)
    secretNum = ''
    for i in range(KOL_CIFR):
        secretNum += str(numbers[i])
    return secretNum

def podskazka(ch_games,ch_secret):
    if ch_games == ch_secret:
        return 'Вы угадали!'

    podskazka = []
    for i in range(len(ch_games)):
        if ch_games[i] == ch_secret[i]:
            podskazka.append('Горячо')
        elif ch_games[i] in ch_secret:
            podskazka.append('Тепло') 

    if len(podskazka) == 0:
        return 'Холодно'

    podskazka.sort()
    return ' '.join(podskazka)       

def proverka_ch(num):
    if num == '':
        return False

    for i in num:
        if i not in '0 1 2 3 4 5 6 7 8 9'.split():
            return False

    return True

def playAgain():
    # Эта функция возвращает True, если игрок хочет сыграть заново, в противном False
    print('Хотите сыграть еще? (да или нет).')
    while True:
        otvet = input()
        otvet = otvet.lower()
        if (otvet == 'да') or (otvet == 'д') or (otvet == 'yes') or (otvet == 'y'):
            # ответ да, запускаем игру по новой
            return True
        elif (otvet == 'нет') or (otvet == 'н') or (otvet == 'no') or (otvet == 'n'):
            # игрок отказался от игры, завершаем
            return False
        else:
            print('''Я вас не понял! 
Введите ответ еще раз.
Введите "да" для продолжения и "нет" для завершения игры''')




# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

print('Я загадаю %s-х значное число, которое вы должны отгадать.' % (KOL_CIFR))
print('Я вам дам несколько подсказок...')
print('Когда я говорю:          Это означает:')
print('  Холодно                Ни одна цифра не отгадана.')
print('  Тепло                  Одна цифра отгадана, но не отгадана позиция')
print('  Горячо                 Одна цифра и ее позиция отгадана.')

while True:
    secretNum = generatorCh()

    print('Итак, я загадал число. У вас есть %s попыток, чтобы отгадать его.' % (KOL_POP))

    popytka = 1
    while popytka <= KOL_POP:
        chislo_games = ''
        while len(chislo_games) != KOL_CIFR or not proverka_ch(chislo_games):
            print('Попытка № %s:' % (popytka))
            chislo_games = input()

        print(podskazka(chislo_games,secretNum))    

        popytka += 1

        if chislo_games == secretNum:
            break
        if popytka > KOL_POP:
            print('Попыток больше не осталось. Я загадал число %s.' % (secretNum))

    if not playAgain():
        break        