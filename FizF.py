def function1():
    print('Первая функция')

def function2():
    print('Попытка вызова функции из функции')
    function1()

function1()
function2()