# ПРОГРАММА "УГАДАЙ ЧИСЛО"
# ПОДКЛЮЧАЕМЫЕ МОДУЛИ ИЛИ ИМПОРТ
import random
# РАЗДЕЛ СОБСТВЕННЫХ ФУНКЦИЙ

# ОСНОВНОГЙ КОД
print('Выберите диапазон чисел')
# выводим на экран сообщение пользователю
print('Введите первое число')
# выводим на экран сообщение пользователю
x = input()
# игрок вводит первое число с которого начинается диапазон выбираемых чисел
x = int(x)
# переводим строки с цифрой в число
print('Введите второе число')
# выводим на экран сообщение пользователю
y = input()
# игрок вводит второе число до которого  выбирается число
y = int(y)
# переводим строку с цифрами в число

print('Введи количество попыток.')
# выводим на экран сообщение пользователю
z = input()
# игрок вводит количество попыток
z = int(z)
# переводим строку с цифрами в число

a = random.randint(x,y)
# программа генерирует случайное число в диапазоне от x до y
c = 0
# присваиваем переменной значение 0
while True:
    # запускаем бесконечный цикл
    print('Я загадала число от '+str(x)+' до '+str(y)+'.')
    # выводим на экран сообщение пользователю с указанием диапазона от x до y
    print('Попробуй отгадай. Введи число.')
    # выводим на экран сообщение пользователю
    c = c + 1
    # увеличиваем счетчик попыток на 1
    b = input()
    # игрок вводит число, пытаясь отгадать загаданное программой
    b = int(b)
    # переводим число в строку
    if a > b:
        # сравниваем два числа: загаданное программой и введенное игроком
        print('Загаданное число больше.')
        # если число больше выводим сообщение об этом
    elif a < b:
        # сравниваем два числа: загаданное программой и введенное игроком
        print('Загаданное число меньше.')
        # если число меньше выводим сообщение об этом
    elif a == b:
        # сравниваем два числа: загаданное программой и введенное игроком
        print('Поздравляю ты угадал.')
        # если числа равны поздравляем игрока, что он угадал
        break
        # прерываем бесконечный цикл
    if c == z:
        # сравниваем счетчик попыток 'c' с числом данных попыток 'z'
        print('Увы, ты не отгадал. Загаданное число '+str(a))
        # если мы достигли количества данных попыток, говорим что игрок проиграл 
        # и сообщаем загаданное программой число
        break
        # прерываем бесконечный цикл
    # окончание бесконечного цикла