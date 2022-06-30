#def fun1():
#    print('Первая функция')

def fun2():
    print('Вторая функция')
    print('Попытка вызвать первую функцию')
    fun1()

def fun1():
    print('Первая функция')

fun1()
fun2()