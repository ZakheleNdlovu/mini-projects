import random
import time

numbers = range(0,50)
lives = 7


def play():
    global lives
    computer_guess = random.choice(numbers)
    while lives > 0:
        print(f"You have {lives} lives remaining")
        try:
            player_guess = int(input('Player guess(0-50): '))
            if player_guess > computer_guess:
                time.sleep(1)
                print('Too high')
                lives = lives-1
            elif player_guess < computer_guess:
                time.sleep(1)
                print('too low')
                lives = lives - 1
            else:
                time.sleep(1)
                print('Correct guess you win')
                break
        except ValueError as e:
            print('Please enter a number')

    else:
        print(f'you are out of lives, game over!\nThe number was {computer_guess}')

def play_again():
    while True:
        ans = input('Do you want to play again?(press (y) for yes, (n) for no): ')
        if ans.lower() == 'y':
            play()
        else:
            print('Goodbye!')
            break

play()
play_again()