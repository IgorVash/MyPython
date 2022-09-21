def returnTrue():
    print('Была вызвана функция returnTrue().')
    return True

def returnFalse():
    print('Была вызвана функция returnFalse().')
    return False

print(returnTrue())
print()
print(returnFalse())
print()
print(returnFalse() or returnTrue())
print()
print(returnTrue() or returnFalse())