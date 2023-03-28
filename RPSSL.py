import random
goes = 0
humanwin = 0
computerwin = 0
possiblehand = ['Rock', 'Paper', 'Scissors', 'Lizzard', 'Spock']

def computer_outcomes(listofpossibleoutcomes):
    index = random.randint(0, 4)
    global mygo
    mygo = listofpossibleoutcomes[index]
    return mygo

def human_outcomes(listofpossibleoutcomes):
    yourgo = None
    txt = input('Enter your choice: Rock(R) Paper(P) Scissors(S) Lizzard(L) Spock (SS): ')
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
    if firstgo == 'L':
        yourgo = listofpossibleoutcomes[3]
        print(f'You have chosen {yourgo}')
    if firstgo == 'SS':
        yourgo = listofpossibleoutcomes[4]
        print(f'You have chosen {yourgo}')
    return yourgo


def compare_hand(mygo, yourgo):
    result = None
    if mygo == yourgo:
        print('DRAW!')
    if mygo == possiblehand[0] and yourgo == possiblehand[1]:
        print('Paper Covers Rock YOU WIN!')
        result = True
    if mygo == possiblehand[0] and yourgo == possiblehand[2]:
        print('Rock Blunts paper I WIN!')
        result = False
    if mygo == possiblehand[1] and yourgo == possiblehand[0]:
        print('Paper Covers Rock I WIN!')
        result = False
    if mygo == possiblehand[1] and yourgo == possiblehand[2]:
        print('Paper Cuts Scissors YOU WIN!')
        result = True
    if mygo == possiblehand[2] and yourgo == possiblehand[0]:
        print('Rock Blunts Scissors YOU WIN!')
        result = True
    if mygo == possiblehand[2] and yourgo == possiblehand[1]:
        print('Scissors Cuts Paper I WIN!')
        result = False
#lizard spock
    if mygo == possiblehand[0] and yourgo == possiblehand[3]:
        print('Rock Crushes Lizard I WIN!')
        result = False
    if mygo == possiblehand[0] and yourgo == possiblehand[4]:
        print('Spock Vaporises Rock YOU WIN!')
        result = True
    if mygo == possiblehand[1] and yourgo == possiblehand[3]:
        print('Lizard Eats Paper YOU WIN!')
        result = True
    if mygo == possiblehand[1] and yourgo == possiblehand[4]:
        print('Paper Disproves Spock I WIN!')
        result = False
    if mygo == possiblehand[2] and yourgo == possiblehand[3]:
        print('Scissors Decapitates Lizard I WIN!')
        result = False
    if mygo == possiblehand[2] and yourgo == possiblehand[4]:
        print('Spock Smashes Scissors YOU WIN!')
        result = True
    if mygo == possiblehand[3] and yourgo == possiblehand[0]:
        print('Rock Crushes lizard YOU WIN!')
        result = True
    if mygo == possiblehand[3] and yourgo == possiblehand[1]:
        print('Lizard Eats Paper I WIN!')
        result = False
    if mygo == possiblehand[3] and yourgo == possiblehand[2]:
        print('Scissors Decapitates Lizard YOU WIN!')
        result = True
    if mygo == possiblehand[3] and yourgo == possiblehand[4]:
        print('Lizard Poisons Spock I WIN!')
        result = False
    if mygo == possiblehand[4] and yourgo == possiblehand[0]:
        print('Spock Vaporises Rock I WIN!')
        result = False
    if mygo == possiblehand[4] and yourgo == possiblehand[1]:
        print('Paper Disproves Spock YOU WIN!')
        result = True
    if mygo == possiblehand[4] and yourgo == possiblehand[2]:
        print('Spock Smashes Scissors I WIN!')
        result = False
    if mygo == possiblehand[4] and yourgo == possiblehand[3]:
        print('Lizard Poisons Spock YOU WIN!')
        result = True
    return result


print('LETS PLAY A GAME: ROCK, PAPER, SCISSORS, LIZARD, SPOCK !', '\n', 'BEST OF 7 !')
while goes < 7:

    human = human_outcomes(possiblehand)
    cpu = computer_outcomes(possiblehand)
    print(f'MY GO...1...2...3....\n ...I CHOOSE........ {cpu}')
    goes += 1

    print('ME: ', cpu)
    print('YOU: ', human)
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