import random
x = random.randint(1,2)
print("Выбери, что выпало.")
print("Введи 1, если решка и 2, если орел")
y = input()
y = int(y)
if x==y:
    print("Ты выиграл!")
else:
    print("Ты проиграл")