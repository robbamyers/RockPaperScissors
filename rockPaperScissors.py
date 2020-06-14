import random,sys
wins = 0
losses = 0
ties = 0
print('Choose your weapon. Type rock, paper, or scissors.')
while True:
    userWeapon = input()
    if userWeapon == 'rock':
        userWeapon = 1
    elif userWeapon == 'paper':
        userWeapon = 2
    elif userWeapon == 'scissors':
        userWeapon = 3
    else:
        print('Please insert a valid command')
        continue
    computerWeapon = random.randint(1,3)
    if computerWeapon == 1:
        print('ROCK')
    elif computerWeapon == 2:
        print('PAPER')
    elif computerWeapon == 3:
        print('SCISSORS')
    if userWeapon == 1 and computerWeapon == 3:
        wins += 1
        print('Nice job! The current score is human:%s computer:%s' % (wins, losses)) 
    elif userWeapon == 2 and computerWeapon == 1:
        wins += 1
        print('Nice job! The current score is human:%s computer:%s' % (wins, losses))
    elif userWeapon == 3 and computerWeapon == 2:
        wins += 1
        print('Nice job! The current score is human:%s computer:%s' % (wins, losses))
    elif userWeapon == computerWeapon:
        ties += 1
        print('Zinger! We got a tie! The score remains is human:%s computer:%s' % (wins, losses))
    elif userWeapon == 1 and computerWeapon == 2:
        losses += 1
        print('Ouch! That stung. The current score is human:%s computer:%s' % (wins, losses))
    elif userWeapon == 2 and computerWeapon == 3:
        losses += 1
        print('Ouch! That stung. The current score is human:%s computer:%s' % (wins, losses))
    elif userWeapon == 3 and computerWeapon == 1:
        losses += 1
        print('Ouch! That stung. The current score is human:%s computer:%s' % (wins, losses))
    if losses >= 2:
        print('You lose! Would you like to play again? Type Y/N')
        replayInput = input()
        if replayInput == 'Y':
            wins = 0
            losses = 0
            ties = 0
            print('Choose your weapon. Type rock, paper, or scissors.')
            continue
        else: sys.exit()
    elif wins >= 2:
        print('You win! Would you like to play again? Type Y/N')
        replayInput = input()
        if replayInput == 'Y':
            wins = 0
            losses = 0
            ties = 0
            print('Choose your weapon. Type rock, paper, or scissors.')
            continue
        else: sys.exit()

       
