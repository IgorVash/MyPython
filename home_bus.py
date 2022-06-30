# Вводим n - кол-во детей, m - кол-во взрослых, k - кол-во людей, которые поместятся в 1 автобусе
n = int(input('Введите общее количество детей\n'))
m = int(input('Введите общее количество взрослых\n'))
k = int(input('Введите сколько человек помещается в 1 автобус\n'))

# Вспомогательные данные: Посчитаем сколько автобусов потребуется для детей
if k < 3:
    d = 0
else:
    if (n%(k-2))!=0:
        d = (n//(k-2))+1
    else:
        d = (n//(k-2))
#print(d)

# Если в автобус помещается меньше трех человек, то ни один ребенок не сможет сесть в автобус
if k<3:
    print('0')
# если количество взрослых //2 менше количества количества автобусов для детей мы не сможем уехать
elif (m//2)<d:
    print('0')
else:
    a = (m+n)//k
    if ((m+n)%k)!=0:
        a += 1
    print(a)