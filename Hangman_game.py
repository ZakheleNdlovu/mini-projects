import string
import random

words = ['good', 'bad','photosynthesis','quarterback','undertaker','center','telescope','international']
computer_play = random.choice(words)
lives = 5
let = []
clue = [letter if letter in let else '-' for letter in computer_play]
print(' '.join(clue))
while lives != 0:
    player = input('letter: ')
    let.append(player)
    word_list = [letter if letter in let else '-' for letter in computer_play]
    print(' '.join(word_list))
    print('Used letters: ','-'.join(let))
    if player == computer_play:
        print('you win!')
        break
    if lives == 5:
        print('                     |  ')
        print('                     |  ')
        print('                     |  ')
        print('                     |  ')
        print('   ________|  ')
    if lives == 4:
        print('    ________  ')
        print('   |                 |  ')
        print('                     |  ')
        print('                     |  ')
        print('   ________|  ')
    if lives == 3:
        print('    ________  ')
        print('    |                 |  ')
        print('    0                |  ')
        print('    |                 |  ')
        print('                      |  ')
        print('                      |  ')
        print('   ________ |  ')
    if lives == 2:
        print('      ________  ')
        print('      |                   |  ')
        print('      0                  |  ')
        print('    / | \               |  ')
        print('                          |  ')
        print('   __________|  ')
    if lives == 1:
        print('      _________  ')
        print('     |                    |  ')
        print('     0                   |  ')
        print('    /|\                 |  ')
        print('     /                   |  ')
        print('    __________|  ')

    if player in computer_play:
        if (''.join(word_list)) == computer_play:
            print('you win!')
            print('Winning word: ',''.join(word_list).upper())
            break
        print('Used letters: ', '-'.join(let))
        print(' '.join(word_list))
        print('correct letter')

    elif player not in computer_play:
        lives = lives - 1
        print('Used letters/words: ', '-'.join(let).upper())
        print('incorrect letter')
        print(lives)



else:
    print('      _________  ')
    print('      |                    |  ')
    print('      0                   |  ')
    print('     /|\                 |  ')
    print('      /\                  |  ')
    print('    __________ |  ')
    print('Winning word: ', computer_play.upper())
    print('game over') 
