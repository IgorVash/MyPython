def proverka(stroka):
    while True:
        print('Введите букву:')
        bukva = input()
        bukva = bukva.lower()
        if len(bukva) != 1:
            print('Вы должны вводить только один символ.')
        elif bukva not in 'йцукенгшщзхъфывапролджэячсмитьбю':
            print('Вы должны вводить только русские буквы.')
        elif bukva in stroka:
            print('вы уже называли эту букву.')
        else:
            return bukva


s = 'баран'
print(s[:3])