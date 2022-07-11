print('''Есть уравнение вида "Ax+B=0".
Программа выведет на экран "INF", 
если уравнение имеет беконечное количество решений,
"NO", если уравнение не имеет решения и
значение "х" при одном решении.''')

a = int(input('Введите значение А:    '))
b = int(input('Введите значение B:    '))

if (a == 0) and (b == 0):
    print('INF')
if (a == 0) and (b != 0):
    print('NO')
if (a != 0) and (b%a != 0):
    print('NO')
if (a != 0) and (b%a == 0):
    c = int(-b/a)
    print(c)

#if a == 0:
#    if b == 0:
#        print('INF')
#    elif b !=0:
#        print('NO')
#else:
#    if b%a != 0:
#        print('NO')
#    else:
#        x = -b/a
#        print(x)