import random
goes = 0
humanwin = 0
computerwin = 0
possiblehand = ['Rock', 'Paper', 'Scissors']

def computer_outcomes(listofpossibleoutcomes):
    index = random.randint(0, 2)
    global mygo
    mygo = listofpossibleoutcomes[index]
    return mygo

def human_outcomes(listofpossibleoutcomes):
    yourgo = None
    txt = input('Enter your choice: Rock(R) Paper(P) Or Scissors(S): ')
    firstgo = txt.upper()
    if firstgo == 'R':
        yourgo = listofpossibleoutcomes[0]
        print(f'You have chosen {yourgo}')
    if firstgo == 'P':
        yourgo = listofpossibleoutcomes[1]
        print(f'You have chosen {yourgo}')
    if firstgo == 'S':
        yourgo = listofpossibleoutcomes[2]
        print(f'You have chosen {yourgo}')
    return yourgo


def compare_hand(mygo, yourgo):
    result = None
    if mygo == yourgo:
        print('DRAW!')
    if mygo == possiblehand[0] and yourgo == possiblehand[1]:
        print('Paper covers Rock YOU WIN!')
        result = True
    if mygo == possiblehand[0] and yourgo == possiblehand[2]:
        print('Rock blunts paper I WIN!')
        result = False
    if mygo == possiblehand[1] and yourgo == possiblehand[0]:
        print('Paper covers Rock I WIN!')
        result = False
    if mygo == possiblehand[1] and yourgo == possiblehand[2]:
        print('Paper cuts Scissors YOU WIN!')
        result = True
    if mygo == possiblehand[2] and yourgo == possiblehand[0]:
        print('Rock blunts Scissors YOU WIN!')
        result = True
    if mygo == possiblehand[2] and yourgo == possiblehand[1]:
        print('Scissors cuts Paper I WIN!')
        result = False
    return result


print('LETS PLAY A GAME- ROCK PAPER SCISSORS !', '\n', 'BEST OF THREE !')
while goes < 3:

    human = human_outcomes(possiblehand)
    cpu = computer_outcomes(possiblehand)
    print(f'MY GO...1...2...3....\n ...I CHOOSE........ {cpu}')
    goes += 1

    print('ME', cpu)
    print('YOU', human)
    result = compare_hand(cpu, human)
    if result == True:
        humanwin += 1
    if result == False:
        computerwin += 1
    if result == None:
        humanwin += 1
        computerwin += 1
    print(f'Score:  ME:{computerwin}...YOU:{humanwin}')

if computerwin > humanwin:
    print(f'\n I WIN {computerwin}/{humanwin}')

if computerwin < humanwin:
    print(f'\n YOU WIN {humanwin}/{computerwin}')

if computerwin == humanwin:
    print('DRAW')