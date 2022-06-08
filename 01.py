import random
x = random.randint(1,20)
print('Загадано число от 1 до 20. Попрубуй угадать.')
y = input()
y = int(y)
if x == y:
    print('Поздравляю. Ты угадал.')
elif x > y:
    print('Загаданное число больше.')
else:
    print('Загаданное число меньше.')
#for n in 'строка':
#    print(n)
