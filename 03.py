import random
x = random.randint(1,20)
print('Загадано число от 1 до 20. Попрубуй угадать.')
for i in range(3):
    y = input()
    y = int(y)
    if x > y:
        print('Загаданное число больше.')
    elif x < y:
        print('Загаданное число меньше.')
    else:
        break

if x == y:
    print('Поздравляю. Ты угадал.')
else:
    print('Увы. Загаданное число '+str(x))