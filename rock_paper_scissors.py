import random
import time

def play():
    choice = ["rock", "paper", "scissors"]
    computer = random.choice(choice)

    player = input("Rock,Paper or Scissors?: ").lower()

    while player not in choice:
        player = input("Rock,Paper or Scissors?: ").lower()

    else:
        while True:
            if player == computer:
                print("Player: ", player)
                time.sleep(1)
                print("Computer: ", computer)
                time.sleep(1)
                print("tie!")
                break
            else:
                if player == "rock":
                    if computer == "paper":
                        print("Player: ", player)
                        time.sleep(1)
                        print("Computer: ", computer)
                        time.sleep(1)
                        print("You loose!")
                        break
                    elif computer == "scissors":
                        print("Player: ", player)
                        time.sleep(1)
                        print("Computer: ", computer)
                        time.sleep(1)
                        print("You win")
                        break
                elif player == "paper":
                    if computer == "rock":
                        print("Player: ", player)
                        time.sleep(1)
                        print("Computer: ", computer)
                        time.sleep(1)
                        print("You win!")
                        break
                    elif computer == "scissors":
                        print("Player: ", player)
                        time.sleep(1)
                        print("Computer: ", computer)
                        time.sleep(1)
                        print("You loose!")
                        break
                elif player == "scissors":
                    if computer == "rock":
                        print("Player: ", player)
                        time.sleep(1)
                        print("Computer: ", computer)
                        time.sleep(1)
                        print("You loose!")
                        break
                    elif computer == "paper":
                        print("Player: ", player)
                        time.sleep(1)
                        print("Computer: ", computer)
                        time.sleep(1)
                        print("You win!")
                        break


play()
while True:
    player_again = input("Do you want to play again?\n(yes or no): ").lower()
    if player_again == 'yes':
        play()
    else:
        print('Goodbye')
        break
