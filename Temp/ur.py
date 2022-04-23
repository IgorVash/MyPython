print('''Есть уравнение: 
ax+b=0. 
Посмотрим чему равен x при введенных
значениях a и b.''')
a = input('Введите чило "a"')
b = input('Введите чило "b"')
a = int(a)
b = int(b)

if (a==0 and b==0):
    print('INF')

if (a==0 and b!=0):
    print('NO')

if (a!=0 and b%a!=0):
    print('NO')

if (a!=0 and b%a==0):
    n = int(-b/a)
    print(n)