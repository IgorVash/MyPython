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


def funk(errorB,yB,sicretS):
    print(HANGMAN_PICS[len(errorB)])
    print()
    
    print('Ошибычные буквы:',end=' ')
    for buk in errorB:
        print(buk,end=' ')
    
    print()
    
    leter = '_'*len(sicretS)
    
    for i in range(len(sicretS)):
        if sicretS[i] in yB:
            leter = leter[:i]+sicretS[i]+leter[i+1:]
    
    


erB = 'алку'
yesB = 'о'
siS = 'ворон'

funk(erB,yesB,siS)