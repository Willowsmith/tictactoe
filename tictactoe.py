gameBoard = {'1':' ', '2':' ', '3':' ',
             '4':' ', '5':' ', '6':' ',
             '7':' ', '8':' ', '9':' '}

board_keys = []

for key in gameBoard:
    board_keys.append(key)

def printBoard(board):
    print(board['1'] + '|' + board['2'] + '|' + board['3'])
    print('--+--+--')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('--+--+--')
    print(board['7'] + '|' + board['8'] + '|' + board['9'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(gameBoard)
        print("It's your turn, " + turn + ". Where would you like to make your move?")
        i += 1
        
        move = input()

        if gameBoard[move] == ' ':
            gameBoard[move] = turn
            count += 1
        else:
            print("That spot is already taken. \nWhere would you like to make your move?")
            continue

        if count >= 5:
            if gameBoard['1'] == gameBoard['2'] == gameBoard['3'] != ' ':
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif gameBoard['4'] == gameBoard['5'] == gameBoard['6'] != ' ':
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif gameBoard['7'] == gameBoard['8'] == gameBoard['9'] != ' ':
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['4'] == gameBoard['7'] != ' ':
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif gameBoard['2'] == gameBoard['5'] == gameBoard['8'] != ' ':
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif gameBoard['3'] == gameBoard['6'] == gameBoard['9'] != ' ':
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif gameBoard['3'] == gameBoard['5'] == gameBoard['7'] != ' ':
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
            elif gameBoard['1'] == gameBoard['5'] == gameBoard['9'] != ' ':
                printBoard(gameBoard)
                print("\nGame Over.\n")
                print("**** " + turn + " won. ****")
                break
        if count == 9:
            print("\nGame Over.\n")
            print("It's a tie!")
        
        if turn == 'X':
            turn = 'O'
        else:
            turn = 'X'


    restart = input("Do you wish to play again? (y/n)")

    if restart == "y" or restart == "Y":
        for key in board_keys:
            gameBoard[key] = " "

        game()

game()