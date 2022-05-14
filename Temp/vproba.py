HANGMAN_PICS = ['''
  +---+
      |
      |
      |
     ===''','''
  +---+
  0   |
      |
      |
     ===''','''
  +---+
  0   |
  |   |
      |
     ===''','''
  +---+
  0   |
 /|   |
      |
     ===''','''
  +---+
  0   |
 /|\  |
      |
     ===''','''
  +---+
  0   |
 /|\  |
 /    |
     ===''','''
  +---+
  0   |
 /|\  |
 / \  |
     ===''']

def displayBoard(errorB,yesB,sicretS):
    print(HANGMAN_PICS[len(errorB)])
    print()
    print('Ошибочные буквы:',end=' ')
    for letter in errorB:
        print(letter,end=' ')
    print()
    slovo = '_'*len(sicretS)
    for i in range(len(sicretS)):
        if sicretS[i] in yesB:
            slovo = slovo[:i]+sicretS[i]+slovo[i+1:]
    print(slovo)
    

eB = 'клмфу'
yB = 'о'
sS = 'ворон'

displayBoard(eB,yB,sS)