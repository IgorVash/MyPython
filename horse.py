# ********************************************************
# РАЗДЕЛ ИМПОРТА МОДУЛЕЙ
# ********************************************************

# ********************************************************
# РАЗДЕЛ СОЗДАННЫХ ФУНКЦИЙ
# ********************************************************

def zastavka():
    print()
    print('******************************************************************')
    print('       /\/\    $$$$$   $$   $$   $$$$$   $$   $$  $$   $$  $$   $$')
    print('      /    \  $$   $$  $$  $$   $$   $$  $$   $$  $$  $$   $$  $$$')
    print('    ~/(^  ^)  $$       $$$$     $$$$$$$   $$$$$$  $$$$     $$ $ $$')   
    print('   ~/  )  (   $$   $$  $$  $$   $$   $$       $$  $$  $$   $$$  $$')
    print('  ~/   (  )    $$$$$   $$   $$  $$   $$       $$  $$   $$  $$   $$')
    print(' ~/     ~~    ----------------------------------------------------')
    print('~/       |           ВЕРСИЯ 1.0        АВТОР: ИГОРЬ ВАШКЕБА')
    print('******************************************************************')
    print()

def nastroyki():
    while True:
        many = input('Введите сколько денег будет у игрока:   ')
        if not many.isdigit():
            # игрок ввел не только цифры
            print('Вы должны вводить только цифры.')
        else:
            minSt = input('Введите размер минимальной ставки:   ')
            if not minSt.isdigit():
                print('Вы должны вводить только цифры.')

# ********************************************************
# ОСНОВНОЕ ТЕЛО ПРОГРАММЫ
# ********************************************************

zastavka()