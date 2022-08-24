import random
h = [0,0,0,0]
l = [90,90,90,90]
victory = 0
while True:
    for i in range(1,5):
        if l[i-1]>0:
            print(str(i)+' '+'_'*h[i-1]+'*'+'_'*l[i-1])
            hp = random.randint(1,3)
            h[i-1] = h[i-1] + hp
            l[i-1] = l[i-1] - hp
        else:
            if victory == 0:
                victory = i
            print(str(i)+' '+'_'*90+'*')

#        if not h[i-1]<90:
#            print('Лошадь '+str(i)+' закончила гонку.')         
    print()
    print()
    if (not h[0]<90) and (not h[1]<90) and (not h[2]<90) and (not h[3]<90):
        for i in range(1,5):
            print(str(i)+' '+'_'*90+'*')
        break

print('Выиграла лошадь '+str(victory))