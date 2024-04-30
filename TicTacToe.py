import random

running = True
winner = None

board = [' ', ' ', ' ',
         ' ', ' ', ' ',
         ' ', ' ', ' ']


def printBoard():
    print('+-----------+')
    print('| ' + board[0] + ' | ' + board[1] + ' | ' + board[2] + ' |')
    print('+---+---+---+')
    print('| ' + board[3] + ' | ' + board[4] + ' | ' + board[5] + ' |')
    print('+---+---+---+')
    print('| ' + board[6] + ' | ' + board[7] + ' | ' + board[8] + ' |')
    print('+-----------+')


def horizWin():
    global running
    global winner
    if board[0] == board[1] == board[2] and board[0] != ' ':
        winner = board[0]
        print('Winner is ', winner)
        printBoard()
        running = False

    elif board[3] == board[4] == board[5] and board[3] != ' ':
        winner = board[3]
        printBoard()
        print('Winner is ', winner)
        running = False

    elif board[6] == board[7] == board[8] and board[6] != ' ':
        winner = board[6]
        printBoard()
        print('Winner is ', winner)
        running = False


def vertnDiagWin():
    global running
    global winner
    if board[0] == board[3] == board[6] and board[0] != ' ':
        winner = board[0]
        printBoard()
        print('Winner is ', winner)
        running = False

    elif board[0] == board[4] == board[8] and board[0] !=' ':
        winner = board[0]
        printBoard()
        print('Winner is ', winner)
        running = False

    elif board[2] == board[4] == board[6] and board[2] !=' ':
        winner = board[2]
        printBoard()
        print('Winner is ', winner)
        running = False

    elif board[1] == board[4] == board[7] and board[1] != ' ':
        winner = board[1]
        printBoard()
        print('Winner is ', winner)
        running = False
    elif board[2] == board[5] == board[8] and board[2] != ' ':
        winner = board[2]
        printBoard()
        print('Winner is ', winner)
        running = False


def diagWin():
    global running
    global winner

    if  board[0] != ' ':
        pass
    elif board[0] == board[4] == board[8] :
        winner = board[0]
        print('Winner is ', winner)
        running = False
    elif board[2] == board[4] == board[6]:
        winner = board[2]
        print('Winner is ', winner)
        running = False


def playPlayer():
    global running
    printBoard()

    player = int(input('choose from box 1 to box 9: '))
    if player > 0 and player < 10:
        if board[player - 1] == ' ':
            board[player - 1] = str('x')

        else:
            print('Square already taken')
            printBoard()


def compPlay():
    while True:
        computer = random.randint(1, 9)
        if board[computer - 1] == ' ':
            board[computer - 1] = str('o')
            break

        elif board[computer - 1] != ' ':
            continue


while running:
    playPlayer()

    horizWin()

    vertnDiagWin()

    compPlay()

    horizWin()

    vertnDiagWin()



