#Tic Tac Toe

import random

def drawBoard(board):
    """Drawing the tic tac toe board"""

    print(board[7] + '|' + board[8] + '|' + board[9])
    print('-+-+-')
    print(board[4] + '|' + board[5] + '|' + board[6])
    print('-+-+-')
    print(board[1] + '|' + board[2] + '|' + board[3])


def inputPlayerLetter():
    """Asking the player to choose a letter"""
    
    letter = ''
    
    while not (letter == 'X' or letter == 'O'):
        print('Do you want to be X or O?')
        letter = input().upper()

    if letter == 'X':
        return ['X', 'O']
    else:
        return ['O', 'X']
    

def whoGoesFirst():
    """Deciding who will play the first move"""

    if random.randint(0, 1) == 0:
        return 'computer'
    else:
        return 'player'
    

def makeMove(board, letter, move):
    """Deploying the move on the grid"""
    board[move] = letter


def isWinner(bo, le):
    """Decides how to win the game by Describing all the possible ways to win the game"""

    return((bo[7] == le and bo[8] == le and bo[9] == le) or
           (bo[4] == le and bo[5] == le and bo[6] == le) or
           (bo[1] == le and bo[2] == le and bo[3] == le) or
           (bo[7] == le and bo[4] == le and bo[1] == le) or
           (bo[8] == le and bo[5] == le and bo[2] == le) or
           (bo[9] == le and bo[6] == le and bo[3] == le) or
           (bo[7] == le and bo[5] == le and bo[3] == le) or
           (bo[9] == le and bo[5] == le and bo[1] == le))


def getBoardCopy(board):
    """Make a copy of board for computer hypothetical analysis"""

    boardCopy = []

    for i in board:
        boardCopy.append(i)
    return boardCopy


def isSpaceFree(board, move):
    """Helper function to check if there is space on the game grid"""
    return board[move] == ' '


def getPlayerMove(board):
    """Get the player move"""

    move = ''

    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        print('What\'s your next move? (1-9)')
        move = input()
    return int(move)


def chooseRandomMoveFromList(board, moveList):
    """This return the valid move from the list"""

    possibleMoves = []
    
    for i in moveList:
        if isSpaceFree(board, i):
            possibleMoves.append(i)

    if len(possibleMoves) != 0:
        return random.choice(possibleMoves)
    else:
        return None
    

def getComputerMove(board, computerLetter):
    """AI algorithm implementation to make sure the game becomes competetive"""

    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'

    #Step 1: Check if the computer is winning after a move
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, computerLetter, i)
            if isWinner(boardCopy, computerLetter):
                return i
            
    #Step 2: Check if we need to block the player winning path
    for i in range(1,10):
        boardCopy = getBoardCopy(board)
        if isSpaceFree(boardCopy, i):
            makeMove(boardCopy, playerLetter, i)
            if isWinner(boardCopy, playerLetter):
                return i
            
    #Step 3: Get the corner position first
    move = chooseRandomMoveFromList(board, [1, 3, 7, 9])
    if move != None:
        return move
    
    #Step 4: Get the middle position
    if isSpaceFree(board, 5):
        return 5
    
    #Step 5: Get the remaining position
    return chooseRandomMoveFromList(board, [2, 4, 6, 8])


def isBoardFull(board):
    """Check if the game grid is out of moves"""

    for i in range(1, 10):
        if isSpaceFree(board, i):
            return False
        
    return True



print('Welcome to Tic Tac Toe!')

while True:

    theBoard = [' '] * 10
    playerLetter , computerLetter = inputPlayerLetter()
    turn = whoGoesFirst()
    print(f'The {turn} will go first.')
    gameIsPlaying = True

    while gameIsPlaying:

        if turn == 'player':
            drawBoard(theBoard)
            move = getPlayerMove(theBoard)
            makeMove(theBoard, playerLetter, move)

            if isWinner(theBoard, playerLetter):
                drawBoard(theBoard)
                print('Horaay! You have won the game.')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie')
                    break
                else:
                    turn = 'computer'

        else:
            move = getComputerMove(theBoard, computerLetter)
            makeMove(theBoard, computerLetter, move)

            if isWinner(theBoard, computerLetter):
                drawBoard(theBoard)
                print('The computer has beaten you! You lose')
                gameIsPlaying = False

            else:
                if isBoardFull(theBoard):
                    drawBoard(theBoard)
                    print('The game is a tie!')
                    break
                else:
                    turn = 'player'

    print('Do you want to play again? (Yes or no)')
    if not input().lower().startswith('y'):
        break